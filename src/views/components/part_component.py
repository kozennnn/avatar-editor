import pygame
from src.data import SpriteSheet, Node


class PartComponent:
    def __init__(self, x: int, y: int, id: int, name: str, spritesheet: SpriteSheet, tree: Node, selected: bool = False) -> None:
        self.x = x
        self.y = y
        self.id = id
        self.name = name
        self.spritesheet = spritesheet
        self.tree = tree
        self.selected = selected
        self.rect = pygame.Rect(x, y, 49, 49)

    def render(self, window: pygame.Surface) -> None:
        self.background = pygame.image.load("./resources/textures/part_background.png").convert_alpha()
        if self.selected:
            self.background = pygame.image.load("./resources/textures/part_selected_background.png").convert_alpha()
        window.blit(self.background, (self.x, self.y))
        sprite = self.spritesheet.get_sprite(self.name)
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * 0.2, sprite.get_height() * 0.2))
        window.blit(sprite, (self.x, self.y))

    def mouseover(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def click(self) -> None:
        print(self.name)
        if self.selected:
            # Remove
            self.tree.remove(self.id)
            self.selected = False
        else:
            self.tree.insert(self.id)
            self.selected = True


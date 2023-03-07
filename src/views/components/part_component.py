import pygame
from src.data import SpriteSheet


class PartComponent:
    def __init__(self, x: int, y: int, name: str, spritesheet: SpriteSheet, selected: bool = False) -> None:
        self.x = x
        self.y = y
        self.name = name
        self.spritesheet = spritesheet
        self.selected = selected

    def render(self, window: pygame.Surface) -> None:
        background = pygame.image.load("./resources/textures/part_background.png").convert_alpha()
        if self.selected:
            background = pygame.image.load("./resources/textures/part_selected_background.png").convert_alpha()
        window.blit(background, (self.x, self.y))
        sprite = self.spritesheet.get_sprite(self.name)
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * 0.2, sprite.get_height() * 0.2))
        window.blit(sprite, (self.x, self.y))


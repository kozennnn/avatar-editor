import pygame
from .components import GridPartComponent
from src.data import SpriteSheet, Node


class EditorView:
    def __init__(self, parts: {}) -> None:
        self.parts = parts

    def render(self, window: pygame.Surface) -> None:
        background = pygame.image.load("./resources/textures/editor_background.png").convert()
        window.blit(background, (0, 0))
        sheet = SpriteSheet("./resources/spritesheets/spritesheet_default.png",
                                 "./resources/spritesheets/spritesheet_default.xml")

        arbre = Node(value=4)
        arbre.insert(22)
        arbre.insert(54)
        arbre.insert(83)
        arbre.insert(85)
        arbre.insert(90)
        arbre.insert(92)
        arbre.insert(102)

        arbre.insert(109)
        offsetX = 75
        offsetY = 80
        for id in arbre.prefix_course():
            sprite = sheet.get_sprite(self.parts.get(id)["name"])
            sprite = pygame.transform.scale(sprite, (
            sprite.get_width() * self.parts.get(id)["scale"], sprite.get_height() * self.parts.get(id)["scale"]))
            if self.parts.get(id)["flipped"]:
                window.blit(pygame.transform.flip(sprite, True, False), (
                self.parts.get(id)["offsetX"] + self.parts.get(id)["flipX"] + offsetX,
                self.parts.get(id)["offsetY"] + offsetY))
            window.blit(sprite, (self.parts.get(id)["offsetX"] + offsetX, self.parts.get(id)["offsetY"] + offsetY))

        GridPartComponent(310, 35, 6, 5, self.parts, sheet, arbre).render(window)
        #pygame.draw.rect(window, (0, 0, 0), (200, 150, 100, 50))


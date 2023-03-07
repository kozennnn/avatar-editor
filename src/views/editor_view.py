import pygame
from .components import GridPartComponent
from src.data import SpriteSheet, Node

offsetX = 75
offsetY = 80


class EditorView:
    def __init__(self, parts: {}) -> None:
        self.parts = parts
        self.handled = False
        self.tree = Node(value=4)
        self.tree.insert(22)
        self.tree.insert(54)
        self.tree.insert(83)
        self.tree.insert(85)
        self.tree.insert(90)
        self.tree.insert(92)
        self.tree.insert(102)
        self.tree.insert(109)

    def render(self, window: pygame.Surface) -> None:
        window.fill((255, 255, 255))
        background = pygame.image.load("./resources/textures/editor_background.png").convert()
        window.blit(background, (0, 0))
        sheet = SpriteSheet("./resources/spritesheets/spritesheet_default.png",
                                 "./resources/spritesheets/spritesheet_default.xml")

        for id in self.tree.prefix_course():
            sprite = sheet.get_sprite(self.parts.get(id)["name"])
            sprite = pygame.transform.scale(sprite, (
            sprite.get_width() * self.parts.get(id)["scale"], sprite.get_height() * self.parts.get(id)["scale"]))
            if self.parts.get(id)["flipped"]:
                window.blit(pygame.transform.flip(sprite, True, False), (
                self.parts.get(id)["offsetX"] + self.parts.get(id)["flipX"] + offsetX,
                self.parts.get(id)["offsetY"] + offsetY))
            window.blit(sprite, (self.parts.get(id)["offsetX"] + offsetX, self.parts.get(id)["offsetY"] + offsetY))

        self.grid = GridPartComponent(310, 35, 6, 5, self.get_parts_by_category("Details"), sheet, self.tree)
        print(self.get_parts_by_category("Details"))
        self.grid.render(window)

    def get_parts_by_category(self, category: str) -> {}:
        items = {}
        for key, value in self.parts.items():
            if value["category"] == category:
                items[key] = value
        return items

    def handle_events(self) -> None:
        for children in self.grid.childrens:
            if children.mouseover() and pygame.mouse.get_pressed()[0] and not self.handled:
                self.handled = True
                children.click()
            if not pygame.mouse.get_pressed()[0] and self.handled:
                self.handled = False



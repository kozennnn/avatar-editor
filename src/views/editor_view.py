import pygame
from .components import GridPartComponent
from src.data import SpriteSheet, Node

offsetX = 75
offsetY = 80

class EditorView:
    def __init__(self, parts: {}) -> None:
        self.next_button = None
        self.previous_button = None
        self.parts = parts
        self.handled = False
        self.selected_category = 0
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

        self.grid = GridPartComponent(310, 35, 6, 5, self.parts_by_category(self.categories()[self.selected_category]), sheet, self.tree)

        self.previous_button = pygame.Rect(310, 432, 39, 31)
        self.next_button = pygame.Rect(592, 432, 39, 31)
        previous_button = pygame.image.load("./resources/textures/left_button.png").convert_alpha()
        window.blit(previous_button, (310, 432))
        next_button = pygame.image.load("./resources/textures/right_button.png").convert_alpha()
        window.blit(next_button, (592, 432))

        self.grid.render(window)

    def parts_by_category(self, category: str) -> {}:
        items = {}
        for key, value in self.parts.items():
            if value["category"] == category:
                items[key] = value
        return items

    def categories(self) -> [str]:
        categories = []
        for key, value in self.parts.items():
            if categories.count(value["category"]) == 0:
                categories.append(value["category"])
        return categories

    def handle_events(self) -> None:
        if self.next_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.handled:
            self.handled = True
            if self.selected_category + 1 > len(self.categories()) - 1:
                self.selected_category = 0
            else:
                self.selected_category += 1
        if self.previous_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.handled:
            self.handled = True
            if self.selected_category - 1 < 0:
                self.selected_category = len(self.categories()) - 1
            else:
                self.selected_category -= 1
        for children in self.grid.childrens:
            if children.mouseover() and pygame.mouse.get_pressed()[0] and not self.handled:
                self.handled = True
                children.click()
            if not pygame.mouse.get_pressed()[0] and self.handled:
                self.handled = False



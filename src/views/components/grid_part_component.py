import pygame
from .part_component import PartComponent
from src.data import SpriteSheet, Node

class GridPartComponent:
    def __init__(self, x: int, y: int, width: int, margin: int, parts: {}, spritesheet: SpriteSheet, tree: Node) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.margin = margin
        self.parts = parts
        self.spritesheet = spritesheet
        self.tree = tree

    def render(self, window: pygame.Surface) -> None:
        for (index, key) in enumerate(self.parts):
            x = 49 * (index % self.width) + (self.margin) * (index % self.width) + self.x
            y = 49 * (index // self.width) + (self.margin - 4) * (index // self.width) + self.y
            name = self.parts[key]["name"]
            selected = False
            if self.tree.find(key):
                selected = True
            PartComponent(x, y, name, self.spritesheet, selected).render(window)



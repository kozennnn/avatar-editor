import pygame
import xml.etree.ElementTree as ElementTree


class App:

    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Avatar Editor")
        self.window = pygame.display.set_mode((640, 480))
        self.window.fill((255, 255, 255))
        print(self.parts)
    def __del__(self) -> None:
        pygame.quit()

    @property
    def parts(self) -> {}:
        tree = ElementTree.parse("./resources/bodydata.xml")
        map = {}
        for node in tree.iter():
            if node.attrib.get("id"):
                id = int(node.attrib.get("id"))
                map[id] = {}
                map[id]["name"] = node.attrib.get("name")
                map[id]["flipped"] = node.attrib.get("flipped") is not None
                if node.attrib.get("offsetX"):
                    map[id]["offsetX"] = int(node.attrib.get("offsetX"))
                else:
                    map[id]["offsetX"] = 0
                if node.attrib.get("offsetY"):
                    map[id]["offsetY"] = int(node.attrib.get("offsetY"))
                else:
                    map[id]["offsetY"] = 0
                if node.attrib.get("flipX"):
                    map[id]["flipX"] = int(node.attrib.get("flipX"))
                else:
                    map[id]["flipX"] = 0
                if node.attrib.get("scale"):
                    map[id]["scale"] = float(node.attrib.get("scale"))
                else:
                    map[id]["scale"] = 1
        return map

    def run(self) -> None:
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

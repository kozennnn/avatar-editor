import pygame
import xml.etree.ElementTree as ElementTree
from .editor_view import EditorView


class App:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Avatar Editor")
        self.window = pygame.display.set_mode((640, 480))
        self.window.fill((255, 255, 255))
        self.render()

    def __del__(self) -> None:
        pygame.quit()

    @property
    def parts(self) -> {}:
        tree = ElementTree.parse("./resources/bodydata.xml")
        map = {}
        for node in tree.iter():
            print(node.tag)
            if node.tag == "Category":
                for part in node.iter():
                    if part.attrib.get("id"):
                        id = int(part.attrib.get("id"))
                        map[id] = {}
                        map[id]["name"] = part.attrib.get("name")
                        map[id]["flipped"] = part.attrib.get("flipped") is not None
                        map[id]["category"] = node.attrib.get("name")
                        if part.attrib.get("offsetX"):
                            map[id]["offsetX"] = int(part.attrib.get("offsetX"))
                        else:
                            map[id]["offsetX"] = 0
                        if part.attrib.get("offsetY"):
                            map[id]["offsetY"] = int(part.attrib.get("offsetY"))
                        else:
                            map[id]["offsetY"] = 0
                        if part.attrib.get("flipX"):
                            map[id]["flipX"] = int(part.attrib.get("flipX"))
                        else:
                            map[id]["flipX"] = 0
                        if part.attrib.get("scale"):
                            map[id]["scale"] = float(part.attrib.get("scale"))
                        else:
                            map[id]["scale"] = 1
        return map

    def render(self) -> None:
        self.editor = EditorView(self.parts)
        self.editor.render(self.window)

    def run(self) -> None:
        running = True
        while running:
            self.editor.render(self.window)
            pygame.display.flip()
            self.editor.handle_events()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

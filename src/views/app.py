import pygame
import time


class App:

    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Avatar Editor")
        self.window = pygame.display.set_mode((640, 480))
        self.window.fill((255, 255, 255))

    def __del__(self) -> None:
        pygame.quit()

    def run(self) -> None:
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

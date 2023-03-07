import pygame


class EditorView:
    def render(self, window: pygame.Surface) -> None:
        pygame.draw.rect(window, (0, 0, 0), (200, 150, 100, 50))


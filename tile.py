import pygame
class Tile:
    def __init__(self, x: int, y: float, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
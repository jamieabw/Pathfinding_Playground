import pygame
from enum import Enum

class Tile:
    def __init__(self, x: int, y: float, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.__type = "EMPTY"
        self.previous = None

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_type(self, type: str):
        self.__type = type

    def get_type(self) -> str:
        return self.__type
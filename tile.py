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
        self.__cost = float("INF")
        self.__previous = None

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_type(self, type: str):
        self.__type = type

    def get_type(self) -> str:
        return self.__type
    
    def get_cost(self) -> int:
        return self.__cost
    
    def set_cost(self, new_cost: int):
        self.__cost = new_cost

    def get_previous(self) -> Tile:
        return self.__previous
    
    def set_previous(self, new_previous):
        self.__previous = new_previous
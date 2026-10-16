import pygame
from tile import Tile

class Map:
    def __init__(self, screen):
        self.screen = screen 
        self.map_size = (48,48)
        self.tiles = []
        for y in range(self.map_size[1]):
            tile_row = []
            for x in range(self.map_size[0]):
                tile_row.append(Tile(x * (pygame.display.get_window_size()[0] // self.map_size[0]), 
                                     y * (pygame.display.get_window_size()[1] // self.map_size[1]),
                                     (pygame.display.get_window_size()[0] // self.map_size[0]) + 1, (pygame.display.get_window_size()[1] // self.map_size[1]) +1))
                
            self.tiles.append(tile_row)


    def run(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[0])):
                pygame.draw.rect(self.screen, (255,255,255),self.tiles[y][x].get_rect())
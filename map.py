import pygame
from tile import Tile


DEFAULT_MAP_SIZE = (16,16)
DEFAULT_START_TILE = (0,0)
DEFAULT_GOAL_TILE = (DEFAULT_MAP_SIZE[0] -1, DEFAULT_MAP_SIZE[1]-1)

class Map:
    def __init__(self, screen):
        self.screen = screen 
        self.map_size = DEFAULT_MAP_SIZE
        self.tiles = []
        for y in range(self.map_size[1]):
            tile_row = []
            for x in range(self.map_size[0]):
                tile_row.append(Tile(x * (pygame.display.get_window_size()[0] // self.map_size[0]), 
                                     y * (pygame.display.get_window_size()[1] // self.map_size[1]),
                                     (pygame.display.get_window_size()[0] // self.map_size[0])-1, (pygame.display.get_window_size()[1] // self.map_size[1])-1)) # -1 to leave a visible gap between

            self.tiles.append(tile_row)
        self.tiles[DEFAULT_START_TILE[0]][DEFAULT_START_TILE[1]].set_type("START")
        self.tiles[DEFAULT_GOAL_TILE[0]][DEFAULT_GOAL_TILE[1]].set_type("GOAL")


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            self.tiles[y // (pygame.display.get_window_size()[1] // self.map_size[1])][x // (pygame.display.get_window_size()[0] // self.map_size[0])].set_type("WALL")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            self.tiles[y // (pygame.display.get_window_size()[1] // self.map_size[1])][x // (pygame.display.get_window_size()[0] // self.map_size[0])].set_type("EMPTY")
        
            


    def run(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[0])):
                tile = self.tiles[y][x]
                colour = (255,255,255)
                if tile.get_type() == "WALL":
                    colour = (0,0,0)
                elif tile.get_type() == "GOAL":
                    colour = (0,255,0)
                elif tile.get_type() == "START":
                    colour = (0,0,255)
                pygame.draw.rect(self.screen, colour, self.tiles[y][x].get_rect())

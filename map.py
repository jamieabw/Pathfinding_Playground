import pygame
from tile import Tile
from config import DEFAULT_GOAL_TILE, DEFAULT_MAP_SIZE, DEFAULT_START_TILE
from a_star_algorithm import A_Star_Algorithm
from bfs import BFS
from dfs import DFS

TILE_COLOUR_MAP = {"WALL" : (0,0,0), "EMPTY" : (255,255,255), "START" : (0,255,0),
                   "GOAL" : (255,0,0), "PATH" : (0,0,255), "EXPLORED" : (100,0,100), "CHECKING" : (100,100,0)}

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
        self.goal_tile = (DEFAULT_GOAL_TILE[1], DEFAULT_GOAL_TILE[0])
        self.start_tile = (DEFAULT_START_TILE[1], DEFAULT_START_TILE[0])
        self.tiles[self.start_tile[0]][self.start_tile[1]].set_type("START")
        self.tiles[self.goal_tile[0]][self.goal_tile[1]].set_type("GOAL")


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            self.tiles[y // (pygame.display.get_window_size()[1] // self.map_size[1])][x // (pygame.display.get_window_size()[0] // self.map_size[0])].set_type("WALL")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            self.tiles[y // (pygame.display.get_window_size()[1] // self.map_size[1])][x // (pygame.display.get_window_size()[0] // self.map_size[0])].set_type("EMPTY")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                A_Star_Algorithm.run_search(self.tiles, self.start_tile, self.goal_tile, self)
            if event.key == pygame.K_b:
                BFS.run_search(self.tiles, self.start_tile, self.goal_tile, self)
            if event.key == pygame.K_d:
                DFS.run_search(self.tiles, self.start_tile, self.goal_tile, self)
            #DFS.run_search(self.tiles, (0,0), (15,15), self)
            if event.key == pygame.K_s:
                x, y = pygame.mouse.get_pos()
                tile_y = y // (pygame.display.get_window_size()[1] // self.map_size[1])
                tile_x = x // (pygame.display.get_window_size()[0] // self.map_size[0])
                self.tiles[self.start_tile[0]][self.start_tile[1]].set_type("EMPTY")
                self.start_tile = (tile_y,tile_x)
                self.tiles[tile_y][tile_x].set_type("START")
            if event.key == pygame.K_g:
                x, y = pygame.mouse.get_pos()
                tile_y = y // (pygame.display.get_window_size()[1] // self.map_size[1])
                tile_x = x // (pygame.display.get_window_size()[0] // self.map_size[0])
                self.tiles[self.goal_tile[0]][self.goal_tile[1]].set_type("EMPTY")
                self.goal_tile = (tile_y,tile_x)
                self.tiles[tile_y][tile_x].set_type("GOAL")

    def reset_explored(self):
        for tiles in self.tiles:
            for tile in tiles:
                tile.set_previous(None)
                tile.set_cost(float("INF"))
                if tile.get_type() == "EXPLORED" or tile.get_type() == "PATH" or tile.get_type() == "CHECKING":
                    tile.set_type("EMPTY")
        self.tiles[self.start_tile[0]][self.start_tile[1]].set_cost(0)

            


    def run(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[0])):
                tile = self.tiles[y][x]
                colour = TILE_COLOUR_MAP[tile.get_type()]
                pygame.draw.rect(self.screen, colour, self.tiles[y][x].get_rect())
                pygame.display.flip()

    def build_path(self, starting_tile_index: tuple[int], goal_tile_index: tuple[int]):
            goal_tile = self.tiles[goal_tile_index[0]][goal_tile_index[1]]
            starting_tile = self.tiles[starting_tile_index[0]][starting_tile_index[1]]
            tile = goal_tile.get_previous()
            while tile != starting_tile and tile != None:
                tile.set_type("PATH")
                tile = tile.get_previous()


    def get_neighbours(self, current_tile_index):
        neighbours: list[Tile] = [None, None, None, None] # top, right, down, left
        y = current_tile_index[0] # top
        x = current_tile_index[1] # bottom
        if (y - 1 >= 0) and (self.tiles[y-1][x].get_type() == "EMPTY" or self.tiles[y-1][x].get_type() == "GOAL"):
            neighbours[0] = (y-1, x)#tiles[y-1][x]
            neighbour = self.tiles[neighbours[0][0]][neighbours[0][1]]
            if neighbour.get_cost() > self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1:
                neighbour.set_cost(self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1)
                neighbour.set_previous(self.tiles[current_tile_index[0]][current_tile_index[1]])

        if  (x + 1 < DEFAULT_MAP_SIZE[1]) and (self.tiles[y][x+1].get_type() == "EMPTY" or self.tiles[y][x+1].get_type() == "GOAL"):
            neighbours[1] = (y, x+1)#tiles[y][x+1]
            neighbour = self.tiles[neighbours[1][0]][neighbours[1][1]]
            if neighbour.get_cost() > self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1:
                neighbour.set_cost(self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1)
                neighbour.set_previous(self.tiles[current_tile_index[0]][current_tile_index[1]])

        if (y + 1 < DEFAULT_MAP_SIZE[0]) and (self.tiles[y+1][x].get_type() == "EMPTY" or self.tiles[y+1][x].get_type() == "GOAL"):
            neighbours[2] = (y+1, x)#tiles[y+1][x]
            neighbour = self.tiles[neighbours[2][0]][neighbours[2][1]]
            if neighbour.get_cost() > self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1:
                neighbour.set_cost(self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1)
                neighbour.set_previous(self.tiles[current_tile_index[0]][current_tile_index[1]])

        if (x-1 >= 0) and (self.tiles[y][x-1].get_type() == "EMPTY" or self.tiles[y][x-1].get_type() == "GOAL"):
            neighbours[3] = (y, x-1)#tiles[y][x-1]
            neighbour = self.tiles[neighbours[3][0]][neighbours[3][1]]
            if neighbour.get_cost() > self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1:
                neighbour.set_cost(self.tiles[current_tile_index[0]][current_tile_index[1]].get_cost() + 1)
                neighbour.set_previous(self.tiles[current_tile_index[0]][current_tile_index[1]])
        
        print(x, y, neighbours)
        return neighbours

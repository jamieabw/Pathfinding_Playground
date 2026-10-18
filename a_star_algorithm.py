import math
from tile import Tile
from config import DEFAULT_GOAL_TILE, DEFAULT_MAP_SIZE, DEFAULT_START_TILE
class A_Star_Algorithm:

    def find_goal(tiles, starting_tile, goal_tile):
        current_tile = starting_tile

    def get_neighbours(tiles, current_tile_index):
        neighbours: list[Tile] = [None, None, None, None] # top, right, down, left
        y = current_tile_index[0] # top
        x = current_tile_index[1] # bottom
        if not (y - 1 < 0) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[0] = tiles[y-1][x]
        if not (x + 1 >= DEFAULT_MAP_SIZE[1] + 1) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[1] = tiles[y][x+1]
        if not (y + 1 < DEFAULT_MAP_SIZE[0]) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[2] = tiles[y+1][x]
        if not (x-1 < 0) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[3] = tiles[y][x-1]
        return neighbours
            



        

    def heuristic(current_tile, goal_tile):
        return math.sqrt(((goal_tile.y - current_tile.y) ** 2) + ((goal_tile.x - current_tile.x) ** 2)) # straight distance between current and target for h(n)
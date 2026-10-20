import math
from tile import Tile
from config import DEFAULT_GOAL_TILE, DEFAULT_MAP_SIZE, DEFAULT_START_TILE
from priority_queue import Priority_Queue
class A_Star_Algorithm:

    def find_goal(tiles, starting_tile, goal_tile):
        current_tile = starting_tile

    def get_neighbours(tiles, current_tile_index):
        neighbours: list[Tile] = [None, None, None, None] # top, right, down, left
        y = current_tile_index[0] # top
        x = current_tile_index[1] # bottom
        if not (y - 1 < 0) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[0] = (y-1, x)#tiles[y-1][x]
        if not (x + 1 >= DEFAULT_MAP_SIZE[1] + 1) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[1] = (y, x+1)#tiles[y][x+1]
        if not (y + 1 < DEFAULT_MAP_SIZE[0]) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[2] = (y+1, x)#tiles[y+1][x]
        if not (x-1 < 0) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[3] = (y, x-1)#tiles[y][x-1]
        return neighbours
            

    def run_search(tiles: list[list[Tile]], starting_tile_index: tuple[int], goal_tile_index: tuple[int]):
        frontier = Priority_Queue(lambda x : tiles[x[1]][x[0]].get_cost() + A_Star_Algorithm.heuristic(tiles[x[1]][x[0]], tiles[goal_tile_index[1]][goal_tile_index[0]]))
        current_tile = starting_tile_index
        while current_tile != goal_tile_index:
            print(current_tile)
            neighbours = A_Star_Algorithm.get_neighbours(tiles, current_tile)
            for neighbour in neighbours:
                if neighbour is None or tiles[neighbour[1]][neighbour[0]].get_type() != "EMPTY":
                    continue
                frontier.enqueue((neighbour[1], neighbour[0]))
                current_tile = frontier.dequeue()
                tiles[current_tile[1]][current_tile[0]].set_type("EXPLORED")



        

    def heuristic(current_tile, goal_tile):
        return math.sqrt(((goal_tile.y - current_tile.y) ** 2) + ((goal_tile.x - current_tile.x) ** 2)) # straight distance between current and target for h(n)
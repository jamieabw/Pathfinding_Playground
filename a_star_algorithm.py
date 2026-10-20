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
        # THIS IS ALL WRONG THE NOT IS PROBABLY EXPANDING OVER THE TWO AND'S FOR EACH OF THESE IF STATEMENTS
        if (y - 1 >= 0) and tiles[y-1][x].get_type() == "EMPTY":
            neighbours[0] = (y-1, x)#tiles[y-1][x]
            neighbour = tiles[neighbours[0][0]][neighbours[0][1]]
            if neighbour.get_cost() > tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1:
                neighbour.set_cost(tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1)
                neighbour.set_previous = tiles[current_tile_index[1]][current_tile_index[0]]

        if  (x + 1 < DEFAULT_MAP_SIZE[1]) and tiles[y][x+1].get_type() == "EMPTY":
            neighbours[1] = (y, x+1)#tiles[y][x+1]
            neighbour = tiles[neighbours[1][0]][neighbours[1][1]]
            if neighbour.get_cost() > tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1:
                neighbour.set_cost(tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1)
                neighbour.set_previous = tiles[current_tile_index[1]][current_tile_index[0]]

        if (y + 1 < DEFAULT_MAP_SIZE[0]) and tiles[y+1][x].get_type() == "EMPTY":
            neighbours[2] = (y+1, x)#tiles[y+1][x]
            neighbour = tiles[neighbours[2][0]][neighbours[2][1]]
            if neighbour.get_cost() > tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1:
                neighbour.set_cost(tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1)
                neighbour.set_previous = tiles[current_tile_index[1]][current_tile_index[0]]

        if (x-1 >= 0) and tiles[y][x-1].get_type() == "EMPTY":
            neighbours[3] = (y, x-1)#tiles[y][x-1]
            neighbour = tiles[neighbours[3][0]][neighbours[3][1]]
            if neighbour.get_cost() > tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1:
                neighbour.set_cost(tiles[current_tile_index[1]][current_tile_index[0]].get_cost() + 1)
                neighbour.set_previous = tiles[current_tile_index[1]][current_tile_index[0]]
        
        print(x, y, neighbours)
        return neighbours
            

    def run_search(tiles: list[list[Tile]], starting_tile_index: tuple[int], goal_tile_index: tuple[int], map):
        t = lambda x : tiles[x[1]][x[0]].get_cost() + A_Star_Algorithm.heuristic(tiles[x[1]][x[0]], tiles[goal_tile_index[1]][goal_tile_index[0]])
        frontier = Priority_Queue(lambda x : tiles[x[1]][x[0]].get_cost() + A_Star_Algorithm.heuristic(tiles[x[1]][x[0]], tiles[goal_tile_index[1]][goal_tile_index[0]]))
        current_tile = starting_tile_index
        tiles[current_tile[1]][current_tile[0]].set_cost(0)
        while current_tile != goal_tile_index:
            #print(current_tile)
            neighbours = A_Star_Algorithm.get_neighbours(tiles, current_tile)
            #print(neighbours)
            for neighbour in neighbours:
                if neighbour is None:
                    continue
                tiles[neighbour[1]][neighbour[0]].set_type("EXPLORED")
                frontier.enqueue((neighbour[1], neighbour[0]))
                if current_tile == goal_tile_index:
                    return
            current_tile = frontier.dequeue()
            print(t(current_tile))
            map.run()
            #print(frontier)

    def heuristic(current_tile, goal_tile):
        return math.sqrt(((goal_tile.y - current_tile.y) ** 2) + ((goal_tile.x - current_tile.x) ** 2)) # straight distance between current and target for h(n)
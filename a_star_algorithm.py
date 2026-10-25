import math
from tile import Tile
from config import DEFAULT_GOAL_TILE, DEFAULT_MAP_SIZE, DEFAULT_START_TILE
from priority_queue import Priority_Queue
class A_Star_Algorithm:

    def run_search(tiles: list[list[Tile]], starting_tile_index: tuple[int], goal_tile_index: tuple[int], map):
        map.reset_explored()
        t = lambda x : tiles[x[0]][x[1]].get_cost() + A_Star_Algorithm.heuristic(tiles[x[1]][x[0]], tiles[goal_tile_index[1]][goal_tile_index[0]])
        frontier = Priority_Queue(lambda x : tiles[x[0]][x[1]].get_cost() + A_Star_Algorithm.heuristic(tiles[x[0]][x[1]], tiles[goal_tile_index[0]][goal_tile_index[1]]))
        current_tile = starting_tile_index
        tiles[current_tile[1]][current_tile[0]].set_cost(0)
        while current_tile != goal_tile_index:
            #print(current_tile)
            neighbours = map.get_neighbours(current_tile)
            # neighbours returns (y, x) so tiles accessed as neighbours[0]neighbours[1]
            #print(neighbours)
            for neighbour in neighbours: 
                if neighbour is None:
                    continue
                frontier.enqueue((neighbour[0], neighbour[1]))
                if current_tile == goal_tile_index:
                    return
                tiles[neighbour[0]][neighbour[1]].set_type("EXPLORED")
            current_tile = frontier.dequeue()
            tiles[current_tile[0]][current_tile[1]].set_type("CHECKING")
            print(t(current_tile))
            tiles[goal_tile_index[0]][goal_tile_index[1]].set_type("GOAL")
            map.run()
        map.build_path(starting_tile_index, goal_tile_index)

    def heuristic(current_tile, goal_tile):
        return math.sqrt(((goal_tile.y - current_tile.y) ** 2) + ((goal_tile.x - current_tile.x) ** 2)) # straight distance between current and target for h(n)
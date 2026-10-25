from tile import Tile
from queue import Queue
from config import DEFAULT_GOAL_TILE
class BFS:
    def run_search(tiles: list[list[Tile]], starting_tile_index: tuple[int], goal_tile_index: tuple[int], map):
        """Performs Breadth First Search to find the optimal path from the starting tile to the goal tile.

        Args:
            tiles (list[list[Tile]]): A 2d list of tiles indexed by their position [y][x].
            starting_tile_index (tuple[int]): The index of the start tile.
            goal_tile_index (tuple[int]): The index of the goal tile.
            map (Map): The environment class.
        """        
        map.reset_explored()
        queue = Queue()
        current_tile = starting_tile_index
        while current_tile != goal_tile_index:
            neighbours = map.get_neighbours(current_tile)
            for neighbour in neighbours:
                if neighbour is None:
                    continue
                queue.enqueue((neighbour[0], neighbour[1]))
                tiles[neighbour[0]][neighbour[1]].set_type("EXPLORED")
            try:
                current_tile = queue.dequeue()
            except Exception:
                print("NO PATH AVAILABLE")
                return
            tiles[current_tile[0]][current_tile[1]].set_type("CHECKING")
            map.run()
            tiles[goal_tile_index[0]][goal_tile_index[1]].set_type("GOAL")
        map.build_path(starting_tile_index, goal_tile_index)

            
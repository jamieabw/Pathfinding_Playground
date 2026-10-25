from tile import Tile
from stack import Stack
class DFS:
    def run_search(tiles: list[list[Tile]], starting_tile_index: tuple[int], goal_tile_index: tuple[int], map):
        """Performs the Depth First Search to find a path from the start tile to the goal tile.

        Args:
            tiles (list[list[Tile]]): A 2d list of tiles indexed by their position [y][x].
            starting_tile_index (tuple[int]): The index of the starting tile.
            goal_tile_index (tuple[int]): The index of the goal tile.
            map (Map): The environment class.
        """        
        map.reset_explored()
        stack = Stack()
        current_tile = starting_tile_index
        while current_tile != goal_tile_index:
            neighbours = map.get_neighbours(current_tile)
            for neighbour in neighbours:
                if neighbour is None:
                    continue
                stack.push((neighbour[0], neighbour[1]))
                tiles[neighbour[0]][neighbour[1]].set_type("EXPLORED")
            try:
                current_tile = stack.pop()
            except Exception:
                print("NO PATH AVAILABLE")
                return
            tiles[current_tile[0]][current_tile[1]].set_type("CHECKING")
            map.run()
            tiles[goal_tile_index[0]][goal_tile_index[1]].set_type("GOAL")
        map.build_path(starting_tile_index, goal_tile_index)

            
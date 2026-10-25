from tile import Tile
from stack import Stack
from config import DEFAULT_GOAL_TILE
class DFS:
    def run_search(tiles: list[list[Tile]], starting_tile_index: tuple[int], goal_tile_index: tuple[int], map):
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
            current_tile = stack.pop()
            tiles[current_tile[0]][current_tile[1]].set_type("CHECKING")
            map.run()
            tiles[goal_tile_index[0]][goal_tile_index[1]].set_type("GOAL")
        map.build_path(starting_tile_index, goal_tile_index)

            
import math
class A_Star_Algorithm:

    def find_goal(tiles, starting_tile, goal_tile):
        current_tile = starting_tile
        

    def heuristic(current_tile, goal_tile):
        return math.sqrt(((goal_tile.y - current_tile.y) ** 2) + ((goal_tile.x - current_tile.x) ** 2)) # straight distance between current and target for h(n)
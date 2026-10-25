# Pathfinding Visualiser

A Python and Pygame project for watching A*, Breadth First Search and Depth First Search find their way through a grid. Place walls, move the start and goal, and compare how each algorithm explores the same map.

## Installation

You will need Python 3.10 or newer and pip installed.

Download and extract this repository, or clone it with Git:

```bash
git clone https://github.com/jamieabw/Pathfinding_Playground.git
cd Pathfinding_Playground
```

Open a terminal in the project folder and install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Running the program

From the project folder, run:

```bash
python main.py
```

On Windows, you can use `py` instead of `python`. On macOS or Linux, you may need to use `python3` for both installation and running the program.

The program opens an 800 × 800 window with a 16 × 16 grid. The start is in the top-left corner and the goal is in the bottom-right corner.

## Controls

Click the program window to give it focus before using the keyboard controls.

| Input | Action |
| --- | --- |
| Left mouse click | Place a wall on the selected tile. |
| Right mouse click | Clear the selected tile. |
| S | Move the start to the tile under the cursor. |
| G | Move the goal to the tile under the cursor. |
| A | Run A* search. |
| B | Run Breadth First Search. |
| D | Run Depth First Search. |
| Window close button | Exit the program. |

Keep the cursor inside the grid when placing the start or goal. Use separate tiles for them, and avoid drawing walls over either marker.

## How to use it

1. Click individual tiles to build walls and create a route through the grid.
2. Hover over a tile and press **S** to choose a starting point.
3. Hover over another tile and press **G** to choose the goal.
4. Press **A**, **B** or **D** to run a search.
5. Watch the tiles change colour as the search progresses. The resulting path is shown in blue.

Running another search clears the previous search colours and path while keeping the walls. Try each algorithm on the same layout to compare the routes and the areas they explore. Right-click walls to remove them, or restart the program for a fresh grid.

## Tile colours

| Colour | Meaning |
| --- | --- |
| White | Empty space. |
| Black | Wall. |
| Green | Start. |
| Red | Goal. |
| Purple | Discovered and added to the search frontier. |
| Olive | Removed from the frontier for checking. |
| Blue | Final path. |

## Algorithms

- **A\*** prioritises tiles using the distance travelled and an estimate of the distance to the goal.
- **Breadth First Search** explores the grid in layers, finding a shortest route when each move has the same cost.
- **Depth First Search** follows a branch before returning to other options. Its route is not necessarily the shortest.

Movement is horizontal and vertical; the searches do not move diagonally.

## Current limitations

Leave a route to the goal when building walls. An unreachable goal is not yet handled gracefully and can cause the search to fail. Searches also run inside the input handler, so the window may not respond to input until a search finishes.

import pygame

class Tile:
    def __init__(self, x: int, y: float, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.__type = "EMPTY"
        self.previous = None
        self.__cost = float("INF")
        self.__previous = None

    def get_rect(self) -> pygame.Rect:
        """Get the rect associated with the tile.

        Returns:
            pygame.Rect: The recet associated with the tile.
        """        
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_type(self, type: str):
        """Set a new type for the tile.

        Args:
            type (str): The new type to give to the tile.
        """        
        self.__type = type

    def get_type(self) -> str:
        """Gives the current type of the tile.

        Returns:
            str: The type of the tile.
        """        
        return self.__type
    
    def get_cost(self) -> int:
        """Get the total cost of the path from the start tile to this tile.

        Returns:
            int: The total cost of the path from the start tile to this tile.
        """        
        return self.__cost
    
    def set_cost(self, new_cost: int):
        """Set a new total cost for the path from the start tile to this tile.

        Args:
            new_cost (int): The new cost value to give to the path from the start tile to this tile.
        """        
        self.__cost = new_cost

    def get_previous(self) -> "Tile | None":
        """Gets the previous tile in the current path

        Returns:
            Tile | None: The previous tile in the path.
        """        
        return self.__previous
    
    def set_previous(self, new_previous: "Tile"):
        """Sets a new tile to be the previous tile in the path when a better path is found.

        Args:
            new_previous (TIle): The new tile to set as the previous tile.
        """        
        self.__previous = new_previous
class Stack:
    def __init__(self):
        self.__contents = []

    def __len__(self):
        return len(self.__contents)

    def peek(self):
        """View the element at the top of the stack.

        Returns:
            any: The item at the top of the stack.
        """        
        return self.__contents[-1]

    def pop(self):
        """Returns and removes the item at the top of the stack.

        Returns:
            any: The item at the top of the stack.
        """        
        return self.__contents.pop(-1)

    def push(self, item):
        """Adds an item to the top of the stack.

        Args:
            item (any): The item you want to place ontop of the stack.
        """        
        self.__contents.append(item)

    def __str__(self):
        result = "[\n"
        for i in range(len(self)-1, -1, -1):
            result += f"{self.__contents[i]}\n"
        return result + "]"


    
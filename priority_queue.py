from queue import Queue
class Priority_Queue(Queue):
    def __init__(self, key):
        super().__init__()
        self.__sort_key = key

    def enqueue(self, item):
        """Places an item in the queue then rearranges order to ensure priority.

        Args:
            item (any): The item to place in the priority queue.
        """        
        super().enqueue(item)
        self._contents.sort(key=self.__sort_key)
from queue import Queue
class Priority_Queue(Queue):
    def __init__(self, key):
        super().__init__()
        self.__sort_key = key

    def enqueue(self, item):
        super().enqueue(item)
        self._contents.sort(key=self.__sort_key)
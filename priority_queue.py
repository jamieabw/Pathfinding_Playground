class Priority_Queue:
    def __init__(self, key):
        self.__contents = []
        self.__sort_key = key

    def enqueue(self, item):
        self.__contents.append(item)
        self.__contents = sorted(self.__contents, key=self.__sort_key)


    def dequeue(self):
        return self.__contents.pop(0)
    
    def __len__(self) -> int:
        return len(self.__contents)
    
    def __str__(self) -> str:
        return f"{self.__contents}"
    

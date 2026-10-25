class Queue:
    def __init__(self):
        self._contents = []

    def enqueue(self, item):
        self._contents.append(item)


    def dequeue(self):
        return self._contents.pop(0)
    
    def __len__(self) -> int:
        return len(self._contents)
    
    def __str__(self) -> str:
        return f"{self._contents}"

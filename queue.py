class Queue:
    def __init__(self):
        self._contents = []

    def enqueue(self, item):
        """Enqueues an item. (adds it to the back of the queue).

        Args:
            item (any): The item to enqueue.
        """        
        self._contents.append(item)


    def dequeue(self):
        """Dequeues the element at the front of the queue

        Returns:
            any: The item at the front of the queue.
        """        
        return self._contents.pop(0)
    
    def __len__(self) -> int:
        return len(self._contents)
    
    def __str__(self) -> str:
        return f"{self._contents}"

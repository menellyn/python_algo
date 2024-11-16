class QueueOnArray:
    def __init__(self, size) -> None:
        self._head = 0
        self._tail = 0
        self._capacity = size
        self._size = 0
        self._queue = [None]*size

    def empty(self) -> bool:
        return self._size == 0

    def full(self) -> bool:
        return self._size == self._capacity


    def enqueue(self, el) -> None:
        if self.full():
            raise Exception("Queue is full")
        self._queue[self._tail] = el
        self._size += 1
        self._tail = (self._tail + 1) % self._capacity


    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty")
        el = self._queue[self._head]
        self._size -= 1
        self._head = (self._head + 1) % self._capacity
        return el


    def size(self) -> int:
        return self._size
    
    def print(self) -> None:
        if self._size == 0:
            return
        ptr = self._head
        print("[begin]", end=" ")
        while ptr != self._tail:
            print(self._queue[ptr], end=" ")
            ptr = (ptr + 1) % self._capacity
        print("[end]")
class DequeOnArray:
    def __init__(self, size) -> None:
        self._front = -1
        self._back = 0
        self._capacity = size
        self._size = 0
        self._deque = [None]*size

    def empty(self) -> bool:
        return self._size == 0

    def full(self) -> bool:
        return self._size == self._capacity

    def push_front(self, el) -> None:
        if self.full():
            raise Exception("Deque is full")
        if self.empty():
            self._back = 0
            self._front = 0
        else:
            self._front = (self._front - 1) % self._capacity
        self._deque[self._front] = el
        self._size += 1


    def push_back(self, el) -> None:
        if self.full():
            raise Exception("Deque is full")
        if self.empty():
            self._back = 0
            self._front = 0
        else:
            self._back = (self._back + 1) % self._capacity
        self._deque[self._back] = el
        self._size += 1

    def pop_front(self):
        if self.empty():
            raise Exception("Deque is empty")
        if self._back == self._front:
            el = self._deque[self._front]
            self._front = -1
            self._back = -1
            self._size = 0
            return el
        el = self._deque[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return el

    def pop_back(self):
        if self.empty():
            raise Exception("Deque is empty")
        if self._back == self._front:
            el = self._deque[self._back]
            self._front = -1
            self._back = -1
            self._size = 0
            return el
        el = self._deque[self._back]
        self._back = (self._back - 1) % self._capacity
        self._size -= 1
        return el

    def front(self):
        if self.empty():
            raise Exception("Deque is empty")
        return self._deque[self._front]

    def back(self):
        if self.empty():
            raise Exception("Deque is empty")
        return self._deque[self._back]

    def size(self) -> int:
        return self._size
    
    def print(self) -> None:
        if self.empty():
            return
        ptr = self._front
        print("[begin]", end=" ")
        while ptr != self._back:
            print(self._deque[ptr], end=" ")
            ptr = (ptr + 1) % self._capacity
        print(self._deque[self._back], end=" ")
        print("[end]")
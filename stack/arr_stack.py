class StackOnArray:
    def __init__(self, size) -> None:
        self._top = -1
        self.capacity = size
        self.stack = [None]*size


    def push(self, el) -> None:
        if self._top == (self.capacity - 1):
            raise Exception("Stack if full")
        self._top += 1
        self.stack[self._top] = el


    def pop(self):
        if self._top == -1:
            raise Exception("Stack is empty")
        el = self.stack[self._top]
        self._top -= 1
        return el


    def top(self):
        if self._top == -1:
            raise Exception("Stack is emmpty")
        return self.stack[self._top]


    def size(self) -> int:
        return self._top + 1


    def empty(self) -> bool:
        return self._top == -1
    
    def print(self) -> None:
        if self._top == -1:
            return
        pos = self._top
        while pos != -1:
            print(self.stack[pos], end=" ")
            pos -= 1
        print()
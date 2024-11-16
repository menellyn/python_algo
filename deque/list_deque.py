class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.prev = None
        self.data = data

class DequeOnList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def empty(self) -> bool:
        return self._head == None and self._tail == None
    
    def push_front(self, el) -> None:
        new_node: Node = Node(el)
        if self.empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1
            return
        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node
        self._size += 1

    def push_back(self, el) -> None:
        new_node: Node = Node(el)
        if self.empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1
            return
        self._tail.next = new_node
        new_node.prev = self._tail
        self._tail = new_node
        self._size += 1

    def pop_front(self):
        if self.empty():
            raise Exception("Deque is empty")
        del_node: Node = self._head
        self._head = self._head.next
        self._size -= 1
        if self._head == None:
            self._tail = None
        else:
            self._head.prev = None
        return del_node.data

    def pop_back(self):
        if self.empty():
            raise Exception("Deque is empty")
        del_node: Node = self._tail
        self._tail = self._tail.prev
        self._size -= 1
        if self._tail == None:
            self._head = None
        else:
            self._tail.next = None
        return del_node.data
    
    def front(self):
        if self.empty():
            raise Exception("Deque is empty")
        return self._head.data

    def back(self):
        if self.empty():
            raise Exception("Deque is empty")
        return self._tail.data

    def size(self) -> int:
        return self._size
    
    def print(self) -> None:
        if self.empty():
            return
        ptr: Node = self._head
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next
        print("None")
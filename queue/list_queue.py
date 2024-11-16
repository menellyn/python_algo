class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class QueueOnList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def empty(self) -> bool:
        return self._size == 0

    def enqueue(self, el) -> None:
        new_node: Node = Node(el)
        if self._head == None:
            self._head = new_node
            self._tail = new_node
            self._size += 1
            return
        self._tail.next = new_node
        self._tail = new_node
        self._size += 1
        

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty")
        del_el: Node = self._head
        self._head = self._head.next
        self._size -= 1
        if self._head == None:
            self._tail == None
        return del_el.data


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

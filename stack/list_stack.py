class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class StackOnLinkedList:
    def __init__(self) -> None:
        self.head = None
        self._size = 0


    def push(self, el) -> None:
        new_node: Node = Node(el)
        new_node.next = self.head
        self.head = new_node
        self._size += 1


    def pop(self):
        if self.head == None:
            raise Exception("Stack is empty")
        del_node: Node = self.head
        self.head = del_node.next
        del_node.next = None
        self._size -= 1
        return del_node.data


    def top(self):
        if self.head == None:
            raise Exception("Stack is empty")
        return self.head.data

    def size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self.head == None

    def print(self) -> None:
        if self.head == None:
            return
        curr_node: Node = self.head
        while curr_node:
            print(curr_node.data, end="->")
            curr_node = curr_node.next
        print("None")
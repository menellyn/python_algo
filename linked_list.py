class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push_front(self, data) -> None:
        node: Node = Node(data)
        node.next = self.head
        self.head = node

    def pop_front(self) -> None:
        if self.head == None:
            return
        node: Node = self.head
        self.head = self.head.next
        del node

    def remove(self, data) -> None:
        if self.head == None:
            return
        if self.head.data == data:
            del_node: Node = self.head
            self.head = None
            del del_node
            return
        prev_node: Node = self.head
        while prev_node.next:
            if prev_node.next.data == data:
                del_node: Node = prev_node.next
                prev_node.next = del_node.next
                del del_node
                return
            prev_node = prev_node.next
        

    def push_back(self, data) -> None:
        node: Node = Node(data)
        if self.head == None:
            self.head = node
            return
        curr_node: Node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = node


    def pop_back(self) -> None:
        if self.head == None:
            return
        del_node: Node = self.head
        if del_node.next == None:
            self.head = None
            del del_node
            return
        while del_node.next.next:
            del_node = del_node.next
        prev_node = del_node
        del_node = del_node.next
        prev_node.next = None
        del del_node
        

    def find(self, data) -> Node:
        curr_node: Node = self.head
        while curr_node:
            if curr_node.data == data:
                break
            curr_node = curr_node.next
        return curr_node


    def print(self) -> None:
        if self.head == None:
            return
        curr_node: Node = self.head
        while curr_node:
            print(curr_node.data, end='->')
            curr_node = curr_node.next
        print("None")

def menu(l: LinkedList) -> None:
    print("----MENU----")
    print("1. Push front", "2. Pop front", sep='\n')
    print("3. Push back", "4. Pop back", sep='\n')
    print("5. Remove element", "6. Find element", sep='\n')
    print("7. Print list", "8. Exit", sep='\n')

    print("------------")

    n = int(input("Enter number of operation: "))

    if n == 1:
        l.push_front(input("Enter data: "))
        menu(l)
    elif n == 2:
        l.pop_front()
        menu(l)
    elif n == 3:
        l.push_back(input("Enter data: "))
        menu(l)
    elif n == 4:
        l.pop_back()
        menu(l)
    elif n == 5:
        l.remove(input("Enter element to delete: "))
        menu(l)
    elif n == 6:
        find_node: Node = l.find(input("Enter element: "))
        if find_node:
            print("True")
        else:
            print("False")
        menu(l)
    elif n == 7:
        l.print()
        menu(l)
    elif n == 8:
        return

if __name__ == "__main__":
    new_list = LinkedList()
    menu(new_list)

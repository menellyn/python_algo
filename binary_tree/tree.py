class Node:
    def __init__(self, key: int, info: str) -> None:
        self.key: int = key
        self.info: str = info
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None

class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None


    def find(self, key: int) -> Node:
        if self.root == None:
            raise Exception("Tree is empty.")

        ptr: Node = self.root

        while ptr:
            if key < ptr.key:
                ptr = ptr.left
            elif key > ptr.key:
                ptr = ptr.right
            else:
                return ptr
            
        return None


    def insert(self, key: int, info: str) -> None:
        node: Node = Node(key, info)

        if self.root == None:
            self.root = node
            return
        
        ptr: Node = self.root
        par: Node = None

        while ptr:
            par = ptr
            if key < par.key:
                ptr = ptr.left
            elif key > par.key:
                ptr = ptr.right
            else:
                break

        if key < par.key:
            par.left = node 
            node.parent = par
        elif key > par.key:
            par.right = node
            node.parent = par
        else:
            par.info = info


    def delete(self, key: int) -> None:
        if self.root == None:
            raise Exception("Tree is empty.")
        
        del_node: Node = self.find(key)

        if not del_node:
            raise Exception("No such key.")
        
        par: Node = del_node.parent

        if (not del_node.left) and (not del_node.right):
            if not par:
                self.root = None
            elif par.left == del_node:
                par.left = None
            else:
                par.right = None
            del del_node
            return
        
        if del_node.left and del_node.right:
            p = del_node.right

            while p.left:
                p = p.left

            p_par: Node = p.parent

            if p.right:
                p.right.parent = p_par
                if p_par.left == p:
                    p_par.left = p.right
                else:
                    p_par.right = p.right
            else:
                if p_par.right == p:
                    p_par.right = None
                else:
                    p_par.left = None
            
            p.parent = par

            if not par:
                self.root = p
            elif par.left == del_node:
                par.left = p
            else:
                par.right = p

            p.left = del_node.left
            p.right = del_node.right
                
            del_node.left.parent = p
            del_node.right.parent = p

            del del_node
            return

        if del_node.left or del_node.right:
            if del_node.left:
                p = del_node.left
            else:
                p = del_node.right

            p.parent = par

            if not par:
                self.root = p
            elif par.left == del_node:
                par.left = p
            else:
                par.right = p

            del del_node
            return


    def find_closer_elem(self, key: int) -> Node | tuple[Node]:
        if self.root == None:
            raise Exception("Tree is empty.")
        
        target: Node = self.find(key)

        if not target:
            raise Exception("No such key.")

        if target.right:
            next: Node = target.right
            while next.left:
                next = next.left
        else:
            curr: Node = target
            next = curr.parent
            while next and next.right == curr:
                curr = next
                next = curr.parent

        if target.left:
            previous: Node = target.left
            while previous.right:
                previous = previous.right
        else:
            curr = target
            previous = curr.parent
            while previous and previous.left == curr:
                curr = previous
                previous = curr.parent
        
        if previous == None:
            return next
        elif next == None:
            return previous
        
        if (key - previous.key) > (next.key - key):
            return next
        elif (key - previous.key) < (next.key - key):
            return previous
        else:
            return (previous, next)


    def _inorder_traversal(self) -> list[Node]:
        stack: list[Node] = []
        sort_elements: list[Node] = []
        ptr: Node = self.root
        stack.append(ptr)

        while stack:
            while ptr.left:
                stack.append(ptr.left)
                ptr = ptr.left

            ptr = stack.pop()
            sort_elements.append(ptr)

            while (not ptr.right) and stack:
                ptr = stack.pop()
                sort_elements.append(ptr)
            
            if ptr.right:
                stack.append(ptr.right)
                ptr = ptr.right

        return sort_elements

    def print(self, key: int = None) -> None:
        if self.root == None:
            raise Exception("Tree is empty.")
        
        elements: list[Node] = self._inorder_traversal()
        if key:
            elements = [x for x in elements if x.key > key]
        
        print(f"{'-'*43:>53}")
        print(f"{'|':>10}", end='')
        print(f"{'key':^20}", end='|')
        print(f"{'info':^20}", end='|')
        print()

        for el in elements:
            print(f"{'-'*43:>53}")
            print(f"{'|':>10}", end='')
            print(f"{el.key:^20}", end='|')
            print(f"{el.info:^20}", end='|')
            print()

        print(f"{'-'*43:>53}")




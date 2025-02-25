from tree import BinaryTree, Node

def display(key: int, info: str) -> None:
    print(f"{'-'*43:>53}")
    print(f"{'|':>10}", end='')
    print(f"{'key':^20}", end='|')
    print(f"{'info':^20}", end='|')
    print()
    print(f"{'-'*43:>53}")
    print(f"{'|':>10}", end='')
    print(f"{key:^20}", end='|')
    print(f"{info:^20}", end='|')
    print()
    print(f"{'-'*43:>53}")

def menu(tree: BinaryTree) -> None:
    print("----MENU----")
    print("1. Add new element", "2. Delete element", sep='\n')
    print("3. Find element", "4. Find closest element", sep='\n')
    print("5. Print table starting from specified key", "6. Print table", sep='\n')
    print("Press any other key to exit")
    print("------------")

    n = int(input("Enter number of operation: "))

    if n == 1:
        while True:
            try:
                key = int(input("Enter key: "))
            except:
                print("Key must be integer.")
            else:
                break
        
        info = input("Enter info: ")
        tree.insert(key, info)
        menu(tree)
    elif n == 2:
        while True:
            try:
                key = int(input("Enter key: "))
            except:
                print("Key must be integer.")
            else:
                break

        try:
            tree.delete(key)
        except Exception as ex:
            print(ex)
        
        menu(tree)
    elif n == 3:
        while True:
            try:
                key = int(input("Enter key: "))
            except:
                print("Key must be integer.")
            else:
                break
        
        try:
            elem: Node = tree.find(key)
        except Exception as ex:
            print(ex)
        else:
            if elem:
                display(elem.key, elem.info)
            else:
                print("No such element")
        
        menu(tree)
    elif n == 4:
        while True:
            try:
                key = int(input("Enter key: "))
            except:
                print("Key must be integer.")
            else:
                break
        
        try:
            elem = tree.find_closer_elem(key)
        except Exception as ex:
            print(ex)
        else:
            if type(elem) is tuple:
                for el in elem:
                    display(el.key, el.info)
            else:
                display(elem.key, elem.info)
        
        menu(tree)
    elif n == 5:
        while True:
            try:
                key = int(input("Enter key: "))
            except:
                print("Key must be integer.")
            else:
                break
        
        try:
            tree.print(key)
        except Exception as ex:
            print(ex)
        
        menu(tree)
    elif n == 6:
        try:
            tree.print()
        except Exception as ex:
            print(ex)
        
        menu(tree)
    else:
        return


if __name__ == "__main__":
    tree: BinaryTree = BinaryTree()
    menu(tree)
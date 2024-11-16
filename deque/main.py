from arr_deque import DequeOnArray
from list_deque import DequeOnList

def menu(deque: DequeOnArray| DequeOnList) -> None:
    print("----MENU----")
    print("1. Push front", "2. Push back", sep="\n")
    print("3. Pop front", "4. Pop back", sep="\n")
    print("5. Get front", "6. Get back", sep="\n")
    print("7. Get size", "8. Print deque", sep="\n")
    print("Press any other key to exit...")

    print("------------")

    n = int(input("Enter number of operation: "))

    if n == 1:
        try:
            deque.push_front(input("Enter data: "))
        except:
            print("Deque is full")
        
        menu(deque)
    elif n == 2:
        try:
            deque.push_back(input("Enter data: "))
        except:
            print("Deque is full")
        
        menu(deque)
    elif n == 3:
        try:
            print(deque.pop_front())
        except:
            print("Deque is empty")
        
        menu(deque)
    elif n == 4:
        try:
            print(deque.pop_back())
        except:
            print("Deque is empty")
        
        menu(deque)
    elif n == 5:
        try:
            print(deque.front())
        except:
            print("Deque is empty")
        
        menu(deque)
    elif n == 6:
        try:
            print(deque.back())
        except:
            print("Deque is empty")
        
        menu(deque)
    elif n == 7:
        print(deque.size())
        menu(deque)
    elif n == 8:
        deque.print()
        menu(deque)
    else:
        return



        
if __name__ == "__main__":
    print("Creating a new deque...")
    print("What type of deque you want to create?")
    print("a. Deque on Array with fix size")
    print("b. Deque on Double Linked List")

    op = input("Enter your choice (a or b): ")

    while op != 'a' or op != 'b':
        if op == 'a':
            while True:
                try:
                    size = int(input("Enter deque size: "))
                    while size <= 0:
                        size = int(input("Incorrect size. Please, enter number > 0: "))
                    break
                except:
                    print("Incorrect size. Please, enter integer.")
            deque = DequeOnArray(size)
            break
        elif op == 'b':
            deque = DequeOnList()
            break
        else:
            op = input("Incorrect choice. Please, enter a or b: ")

    menu(deque)
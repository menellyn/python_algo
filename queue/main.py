from arr_queue import QueueOnArray
from list_queue import QueueOnList

def menu(stack: QueueOnList|QueueOnArray) -> None:
    print("----MENU----")
    print("1. Enqueue", sep='\n')
    print("2. Dequeue", "3. Get size", sep='\n')
    print("4. Is empty?", "5. Print queue", sep='\n')
    print("Press any other key to exit...")

    print("------------")

    n = int(input("Enter number of operation: "))

    if n == 1:
        try:
            queue.enqueue(input("Enter data: "))
        except:
            print("Queue is full")
        menu(queue)
    elif n == 2:
        try:
            print(queue.dequeue())
        except:
            print("Queue is empty")
        menu(queue)
    elif n == 3:
        print(queue.size())
        menu(queue)
    elif n == 4:
        print(queue.empty())
        menu(queue)
    elif n == 5:
        queue.print()
        menu(queue)
    else:
        return



        
if __name__ == "__main__":
    print("Creating a new queue...")
    print("What type of queue you want to create?")
    print("a. Queue on Array with fix size")
    print("b. Queue on Linked List")

    op = input("Enter your choice (a or b): ")

    while op != 'a' or op != 'b':
        if op == 'a':
            while True:
                try:
                    size = int(input("Enter queue size: "))
                    while size <= 0:
                        size = int(input("Incorrect size. Please, enter number > 0: "))
                    break
                except:
                    print("Incorrect size. Please, enter integer.")
            queue = QueueOnArray(size)
            break
        elif op == 'b':
            queue = QueueOnList()
            break
        else:
            op = input("Incorrect choice. Please, enter a or b: ")

    menu(queue)
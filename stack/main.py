from arr_stack import StackOnArray
from list_stack import StackOnLinkedList

def menu(stack: StackOnArray|StackOnLinkedList) -> None:
    print("----MENU----")
    print("1. Push", sep='\n')
    print("2. Pop", "3. Get top element", sep='\n')
    print("4. Get size", "5. Is empty?", sep='\n')
    print("6. Print stack", "7. Exit", sep='\n')

    print("------------")

    n = int(input("Enter number of operation: "))

    if n == 1:
        try:
            stack.push(input("Enter data: "))
        except:
            print("Stack is full")
        menu(stack)
    elif n == 2:
        try:
            print(stack.pop())
        except:
            print("Stack is empty")
        menu(stack)
    elif n == 3:
        try:
            print(stack.top())
        except:
            print("Stack is empty")
        menu(stack)
    elif n == 4:
        print(stack.size())
        menu(stack)
    elif n == 5:
        print(stack.empty())
        menu(stack)
    elif n == 6:
        stack.print()
        menu(stack)
    elif n == 7:
        return



        
if __name__ == "__main__":
    print("Creating a new stack...")
    print("What type of stack you want to create?")
    print("a. Stack on Array with fix size")
    print("b. Stack on Linked List")

    op = input("Enter your choice (a or b): ")

    while op != 'a' or op != 'b':
        if op == 'a':
            stack = StackOnArray(int(input("Enter stack size: ")))
            break
        elif op == 'b':
            stack = StackOnLinkedList()
            break
        else:
            op = input("Incorrect choice. Please, enter a or b: ")

    menu(stack)
    


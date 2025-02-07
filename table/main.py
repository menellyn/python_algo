from table_with_two_keyspace import Table, InfoType

def display(key1: int, key2: str, info: InfoType):
    print(f"{'-'*63:>73}")
    print(f"{'|':>10}", end='')
    print(f"{'key1':^20}", end='|')
    print(f"{'key2':^20}", end='|')
    print(f"{'info':^20}", end='|')
    print()
    print(f"{'-'*63:>73}")
    print(f"{'|':>10}", end='')
    print(f"{key1:^20}", end='|')
    print(f"{key2:^20}", end='|')
    print(f"{info._num1:^20}", end='|')
    print()
    print(f"{'|':>10}", end='')
    print(f"{'':^20}", end='|')
    print(f"{'':^20}", end='|')
    print(f"{info._num2:^20}", end='|')
    print()
    print(f"{'|':>10}", end='')
    print(f"{'':^20}", end='|')
    print(f"{'':^20}", end='|')
    print(f"{info._s:^20}", end='|')
    print()
    print(f"{'-'*63:>73}")

def menu(table: Table) -> None:

    print("----MENU----")
    print("1. Add new element", "2. Find by (key1, key2)", sep='\n')
    print("3. Delete element by (key1, key2)", "4. Find by key1", sep='\n')
    print("5. Find by key2", "6. Delete element by key1", sep='\n')
    print("7. Delete elements by key2", "8. Print table", sep='\n')
    print("9. Find by parent key", "10. Find by key2 and release", sep='\n')
    print("11. Delete by key2 and release", "Press any other key to exit", sep='\n')
    print("------------")

    n = int(input("Enter number of operation: "))

    if n == 1:
        key1 = int(input("Enter key1: "))
        parent = int(input("Enter parent key: "))
        key2 = input("Enter key2: ")
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        s = input("Enter str: ")

        flag = table.add(key1, parent, key2, num1, num2, s)
        if flag == -1:
            print("Table is full")
        elif flag == -2:
            print("Key1 can't be 0")
        elif flag == -3:
            print(f"No such parent key={parent}")
        elif flag == -4:
            print(f"key1={key1} already exists. Key must be unique")
        
        menu(table)
    elif n == 2:
        key1 = int(input("Enter key1: "))
        key2 = input("Enter key2: ")
        info = table.find_by_key1_key2(key1, key2)
        if not info: 
            print("No such key or pair of keys (key1, key2)")
        else:
            display(key1, key2, info)
        
        menu(table)
    elif n == 3:
        key1 = int(input("Enter key1: "))
        key2 = input("Enter key2: ")
        flag = table.delete_by_key1_key2(key1, key2)
        if flag == -1:
            print("No such key")
        elif flag == -2:
            print("No such pair of keys")
        elif flag == -3:
            print("Can't delete, the key1 is a parent key")
        
        menu(table)
    elif n == 4:
        key1 = int(input("Enter key1: "))
        ans = table.find_by_key1(key1)
        if not ans:
            print("No such key")
        else:
            display(key1, ans[0], ans[1])
        menu(table)
    elif n == 5:
        key2 = input("Enter key2: ")
        ans = table.find_by_key2(key2)

        if not ans:
            print("No suck key")
        else:
            ans.print()
        
        menu(table)
    elif n == 6:
        key1 = int(input("Enter key1: "))

        flag = table.delete_by_key1(key1)

        if flag == -1:
            print("No such key")

        menu(table)
    elif n == 7:
        key2 = input("Enter key2: ")
        flag = table.delete_by_key2(key2)
        if flag == -1:
            print("No such key")
        menu(table)
    elif n == 8:
        table.print()
        menu(table)
    elif n == 9:
        parent = int(input("Enter parent key: "))

        ans = table.find_by_parent(parent)
        if not ans:
            print("No such parent key")
        else:
            ans.print()
        menu(table)
    elif n == 10:
        key2 = input("Enter key2: ")
        rel = int(input("Enter release: "))

        ans = table.find_by_key2_rel(key2, rel)
        
        if not ans:
            print("No such key or release")
        else:
            display(ans[0], key2, ans[1])
        menu(table)
    elif n == 11:
        key2 = input("Enter key2: ")
        rel = int(input("Enter release: "))

        flag = table.delete_by_key2_rel(key2, rel)

        if flag == -1:
            print("No such key or release")
        
        menu(table)
    else:
        return
    

if __name__ == "__main__":
    size_ks1, size_ks2 = 30, 10
    my_table: Table = Table(size_ks1, size_ks2)
    my_table.add(1, 0, "str1", 5, 32, "info1")
    my_table.add(3, 0, "str2", 77, 2, "info")
    my_table.add(8, 3, "str1", 51, 312, "info11")

    menu(my_table)

        
        





class InfoType:

    def __init__(self, num1: int, num2: int, s: str):
        self._num1: int = num1
        self._num2: int = num2
        self._s: str = s

class Item:

    def __init__(self, key1: int, key2: str, info: InfoType):
        self._key1: int = key1
        self._key2: str = key2
        self._info: InfoType = info
        self._idx1: int = None
        self._p2: KeySpace2 = None

class KeySpace1:

    def __init__(self) -> None:
        self._key: int = 0
        self._par: int = 0
        self._info: Item = None 

class Node2:

    def __init__(self, info: Item) -> None:
        self._release: int = 0
        self._info: Item = info
        self._next: Node2 = None

    
class KeySpace2:

    def __init__(self, key: str) -> None:
        self._key: str = key
        self._realese_couter: int = 1
        self._elem_counter: int = 1
        self._node: Node2 = None
        self._next: KeySpace2 = None

class Table:

    def __init__(self, msize1: int, msize2: int) -> None:
        self._msize1: int = msize1
        self._msize2: int = msize2
        self._csize1: int = 0
        self._csize2: int = 0
        self._ks1: list[KeySpace1] = [KeySpace1() for _ in range(msize1)]
        self._ks2: list[KeySpace2] = [None for _ in range(msize2)]


    def _hash_func(self, key) -> int:
        h = 0
        for s in key:
            h += ord(s)
        return h % self._msize2


    def _is_parent(self, par: int) -> bool:
        begin = 0
        end = self._csize1 - 1
        while (begin <= end):
            curr = (begin + end) // 2
            if self._ks1[curr]._par == par:
                return True
            elif self._ks1[curr]._par < par:
                begin = curr + 1
            else:
                end = curr - 1
        
        return False


    def _find_in_ks1(self, key: int) -> KeySpace1:
        if self._csize1 == 0:
            return None
        
        if key == 0:
            return None
        
        for el in self._ks1:
            if el._key == key:
                return el
        
        return None


    def _find_in_ks2(self, key: str) -> KeySpace2:
        if self._csize2 == 0:
            return None
        
        init = self._hash_func(key)
        actual = self._ks2[init]

        if actual == None:
            return None
        
        while actual:
            if actual._key == key:
                return actual
            actual = actual._next
        
        return None

    def _find_in_ks2_rel(self, key: str, release: int) -> Node2:
        target_ks = self._find_in_ks2(key)
        if target_ks == None:
            return None
        
        actual_node = target_ks._node

        while actual_node:
            if actual_node._release == release:
                return actual_node
            actual_node = actual_node._next

        return None

    def _add_in_ks1(self, key: int, par: int, info: Item) -> int:
        i = self._csize1

        while i > 0 and self._ks1[i-1]._par > par:
            self._ks1[i]._key = self._ks1[i-1]._key
            self._ks1[i]._par = self._ks1[i-1]._par
            self._ks1[i]._info = self._ks1[i-1]._info
            self._ks1[i]._info._idx1 = i
            i -= 1
        
        self._ks1[i]._key = key
        self._ks1[i]._par = par
        self._ks1[i]._info = info
        self._csize1 += 1

        return i


    def _add_in_ks2(self, key: str, info: Item) -> Node2:
        init = self._hash_func(key)
        new_node = Node2(info)
        actual_ks = self._find_in_ks2(key)

        if actual_ks == None:
            new_key = KeySpace2(key)
            new_node._release = 1
            new_key._node = new_node
            new_key._next = self._ks2[init]
            self._ks2[init] = new_key
        else:
            actual_ks._realese_couter += 1
            actual_ks._elem_counter += 1
            new_node._release = actual_ks._realese_couter
            new_node._next = actual_ks._node
            actual_ks._node = new_node

        self._csize2 += 1
        return new_node
    

    def _delete_from_ks1(self, idx: int) -> None:

        while idx + 1 < self._csize1 and self._ks1[idx+1]._key != 0 :
            self._ks1[idx]._key = self._ks1[idx+1]._key
            self._ks1[idx]._par = self._ks1[idx+1]._par
            self._ks1[idx]._info = self._ks1[idx+1]._info
            self._ks1[idx]._info._idx1 = idx
            idx += 1

        self._ks1[idx]._key = 0
        self._csize1 -= 1

    def _delete_from_ks2(self, key: str, node: Node2) -> int:
        ks2 = self._find_in_ks2(key)
        self._csize2 -= 1

        if ks2._elem_counter == 1:
            del node
            init = self._hash_func(key)
            previous = self._ks2[init]

            if previous._key == key:
                previous = previous._next
                ks2._next = None
                del ks2
                return 0 
            
            while previous._next._key != key:
                previous = previous._next

            previous._next = ks2._next
            ks2._next = None
            del ks2
            return 0
        
        if ks2._node._release == node._release:
            ks2._node = node._next
            node._next = None
            del node
            ks2._elem_counter -= 1
            return 0
        else:
            prev_node = ks2._node

            while prev_node._next._release != node._release:
                prev_node = prev_node._next
            
            prev_node._next = node._next
            node._next = None
            del node
            ks2._elem_counter -= 1
            return 0


    def add(self, key1: int, par: int, key2: str, inf_num1: int, inf_num2: int, inf_s: str) -> int:
        if self._csize1 == self._msize1:
            return -1
        if key1 == 0:
            return -2
        if self._find_in_ks1(par) == None and par != 0:
            return -3
        if self._find_in_ks1(key1) != None:
            return -4

        info = InfoType(inf_num1, inf_num2, inf_s)
        item = Item(key1, key2, info)
        item._idx1 = self._add_in_ks1(key1, par, item)
        item._p2 = self._add_in_ks2(key2, item)
        return 0 
        

    def find_by_key1_key2(self, key1: int, key2: str) -> InfoType:
        ks1 = self._find_in_ks1(key1)
        
        if (ks1 == None) or (self._find_in_ks2(key2) == None) or (ks1._info._key2 != key2):
            return None
        
        return ks1._info._info


    def find_by_key1(self, key: int) -> tuple[str, InfoType]:
        ks1 = self._find_in_ks1(key)
        if ks1 == None:
            return None
        return (ks1._info._key2, ks1._info._info)


    def find_by_key2_rel(self, key: str, rel: int) -> tuple[int, InfoType]:
        node = self._find_in_ks2_rel(key, rel)

        if node == None: 
            return None
        
        return (node._info._key1, node._info._info)


    def find_by_key2(self, key: str):

        actual = self._find_in_ks2(key)
        if actual == None:
            return None

        new_table = Table(self._msize1, self._msize2)

        node = actual._node
        while node != None:
            item: Item = node._info
            new_table.add(item._key1, 0, item._key2, item._info._num1, item._info._num2, item._info._s)
            node = node._next
        
        return new_table


    def find_by_parent(self, par: int):

        if not self._is_parent(par) and par != 0:
            return None
        
        new_table = Table(self._msize1, self._msize2)

        for i in range(self._csize1):
            if self._ks1[i]._par == par:
                item: Item = self._ks1[i]._info
                new_table.add(item._key1, 0, item._key2, item._info._num1, item._info._num2, item._info._s)

        return new_table

    def delete_by_key1_key2(self, key1: int, key2: str) -> int:

        ks1 = self._find_in_ks1(key1)
        ks2 = self._find_in_ks2(key2)

        if (not ks1) and (not ks2):
            return -1
        
        if ks1._info._key2 != key2:
            return -2
        
        if self._is_parent(key1):
            return -3
        
        node = ks1._info._p2
        idx = ks1._info._idx1
        del_item: Item = ks1._info
        del_info = del_item._info
        del del_info
        del del_item

        self._delete_from_ks1(idx)
        self._delete_from_ks2(key2, node)

        return 0
        

    def delete_by_key2_rel(self, key: str, release: int) -> int:

        del_node = self._find_in_ks2_rel(key, release)

        if not del_node:
            return -1 
        
        del_item: Item = del_node._info
        del_info: InfoType = del_item._info
        ks1_idx: int = del_item._idx1

        del del_info
        del del_item

        self._delete_from_ks1(ks1_idx)
        self._delete_from_ks2(key, del_node)

        return 0

    def delete_by_key1(self, key: int) -> int:
        
        ks1 = self._find_in_ks1(key)
        idx = ks1._info._idx1

        if not ks1:
            return -1
        
        del_item: Item = ks1._info
        del_info: InfoType = del_item._info
        del_node: Node2 = del_item._p2
        key2: str = del_item._key2

        del del_info
        del del_item
        self._delete_from_ks1(idx)
        self._delete_from_ks2(key2, del_node)

        return 0


    def delete_by_key2(self, key: str) -> int:
        
        ks2 = self._find_in_ks2(key)

        if not ks2:
            return -1
        
        count = ks2._elem_counter
        for i in range(count):
            del_node = ks2._node
            ks1_idx = del_node._info._idx1
            del_item = del_node._info
            del_info = del_item._info
            self._delete_from_ks1(ks1_idx)
            self._delete_from_ks2(key, del_node)
            del del_info
            del del_item

        return 0

    def print(self) -> None:
        if self._csize1 == 0:
            return

        print(f"{'-'*56:>65}")
        print(f"{'|':>10}", end='')
        print(f"{'key1':^10}", end='|')
        print(f"{'parent':^10}", end='|')
        print(f"{'key2':^10}", end='|')
        print(f"{'ver':^10}", end='|')
        print(f"{'info':^10}", end='|')
        print()
        print(f"{'-'*56:>65}")

        for i in range(self._csize1):
            item: Item = self._ks1[i]._info
            print(f"{'|':>10}", end='')
            print(f"{item._key1:^10}", end='|')
            print(f"{self._ks1[i]._par:^10}", end='|')
            print(f"{item._key2:^10}", end='|')
            print(f"{item._p2._release:^10}", end='|')
            print(f"{item._info._num1:^10}", end='|')
            print()
            print(f"{'|':>10}", end='')
            print(f"{'':^10}", end='|')
            print(f"{'':^10}", end='|')
            print(f"{'':^10}", end='|')
            print(f"{'':^10}", end='|')
            print(f"{item._info._num2:^10}", end='|')
            print()
            print(f"{'|':>10}", end='')
            print(f"{'':^10}", end='|')
            print(f"{'':^10}", end='|')
            print(f"{'':^10}", end='|')
            print(f"{'':^10}", end='|')
            print(f"{item._info._s:^10}", end='|')
            print()
            print(f"{'-'*56:>65}")



        
        
        







        
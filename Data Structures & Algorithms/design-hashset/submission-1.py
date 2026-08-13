class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.set = [ListNode(0) for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        current = self.set[index]

        while current.next:
            if current.next.val == key:
                return
            current = current.next
        
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.set[index]

        while current.next:
            if current.next.val == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        current = self.set[index]

        while current.next:
            if current.next.val == key:
                return True

            current = current.next
        
        return False

    #Another with DirectArray Time: O(1) Space: O(n)

    # def __init__(self):
    #     self.hash=[False]*1000001
        

    # def add(self, key: int) -> None:
    #     self.hash[key]=True

    # def remove(self, key: int) -> None:
    #     self.hash[key]=False

    # def contains(self, key: int) -> bool:
    #     return self.hash[key]
    
    #Another Method with Dynamic Array Time: O(1) (remove O(K)) Space: O(N) (more effecient than ListNode)
    
    # def __init__(self):
    #     self.size = 1000
    #     # Каждая корзина — это отдельный динамический массив (list)
    #     self.set = [[] for _ in range(self.size)]

    # def _hash(self, key: int) -> int:
    #     return key % self.size

    # def add(self, key: int) -> None:
    #     index = self._hash(key)
    #     # Если элемента ещё нет в массиве корзины, добавляем его
    #     if key not in self.set[index]:
    #         self.set[index].append(key)

    # def remove(self, key: int) -> None:
    #     index = self._hash(key)
    #     if key in self.set[index]:
    #         self.set[index].remove(key)

    # def contains(self, key: int) -> bool:
    #     index = self._hash(key)
    #     return key in self.set[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
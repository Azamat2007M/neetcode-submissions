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
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
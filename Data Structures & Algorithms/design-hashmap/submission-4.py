class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        buckets = self.map[index]

        for bucket in buckets:
            if bucket[0] == key:
                bucket[1] = value
                return
        
        buckets.append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        buckets = self.map[index]

        for bucket in buckets:
            if bucket[0] == key:
                return bucket[1]

        return -1
 
    def remove(self, key: int) -> None:
        index = self._hash(key)
        buckets = self.map[index]

        for i, bucket in enumerate(buckets):
            if bucket[0] == key:
                buckets.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
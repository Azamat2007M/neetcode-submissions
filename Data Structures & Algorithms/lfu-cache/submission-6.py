from collections import defaultdict

#DoubleLinkedList method Time: O(1) (get and put) Space: O(n)

class Node:
    def __init__(self, key = 0, val = 0, freq = 1, next = None, prev = None):
        self.key, self.val = key, val
        self.freq = freq
        self.next, self.prev = next, prev

class DoubleLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0
    
    def length(self):
        return self.size
    
    def pushRight(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        self.size += 1

    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next = node.prev = None
        self.size -= 1

    def popLeft(self):
        if self.size == 0: return None
        node = self.left.next
        self.pop(node)
        return node
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCache = 0
        self.nodeMap = {}
        self.linkedList = defaultdict(DoubleLinkedList)

    def counter(self, node):
        ctn = node.freq
        self.linkedList[ctn].pop(node)

        if self.linkedList[ctn].length() == 0:
            del self.linkedList[ctn]
            if ctn == self.lfuCache:
                self.lfuCache += 1
        
        node.freq += 1
        self.linkedList[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self.counter(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return

        if self.cap == len(self.nodeMap):
            node = self.linkedList[self.lfuCache].popLeft()
            self.nodeMap.pop(node.key)

            if self.linkedList[self.lfuCache].length() == 0:
                del self.linkedList[self.lfuCache]
        
        node = Node(key, value)
        self.nodeMap[key] = node
        self.linkedList[1].pushRight(node)
        self.lfuCache = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
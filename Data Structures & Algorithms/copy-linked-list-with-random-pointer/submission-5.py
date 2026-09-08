"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Interleaving Nodes method Time: O(n) Space: O(1)
        if not head:
            return None
            
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
            
        return copy_head

        #Hash map method Time: O(n) Space: O(n)
        # old_copy = {None: None}
        # curr = head

        # while curr:
        #     old_copy[curr] = Node(curr.val)
        #     curr = curr.next
        
        # curr = head

        # while curr:
        #     copy = old_copy[curr]
        #     copy.next = old_copy[curr.next]
        #     copy.random = old_copy[curr.random]
        #     curr = curr.next
        
        # return old_copy[head]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Two Pointers method (tortoise and hare) Time: O(n) Space: O(1)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

        #Hash set method Time: O(n) Space: O(n)
        # visited = set()
        # current = head

        # while current:
        #     if current in visited:
        #         return True
            
        #     visited.add(current)
        #     current = current.next
        
        # return False
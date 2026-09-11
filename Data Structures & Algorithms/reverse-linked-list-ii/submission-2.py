# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Iterative method Time: O(n) Space: O(1)
        if not head or left == right:
            return head

        # dummy = ListNode(0, head)
        # prev = dummy

        # for _ in range(left - 1):
        #     prev = prev.next
        
        # curr = prev.next

        # for _ in range(right - left):
        #     next_node = curr.next
        #     curr.next = next_node.next
        #     next_node.next = prev.next
        #     prev.next = next_node
        
        # return dummy.next

        #A fleeting spirit method Time: O(n) Space: O(1)
        dummy = ListNode(0, head)
        lprev = dummy

        for _ in range(left - 1):
            lprev = lprev.next
        
        curr = lprev.next
        prev = None

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        
        lprev.next.next = curr
        lprev.next = prev

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        dummy = ListNode(0, head)
        prev_node = dummy

        while True:
            kth = self.get_kth(prev_node, k)

            if not kth:
                break
            
            next_node = kth.next
            prev, curr = kth.next, prev_node.next
            
            while curr != next_node:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_node.next
            prev_node.next = kth
            prev_node = tmp
        
        return dummy.next
    
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Iterative method Time: O(n) Space: O(1)
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

        # Recursive method Time: O(n) Space: O(n/k)
        # curr = head
        # count = 0

        # while curr and count < k:
        #     curr = curr.next
        #     count += 1

        # if count < k:
        #     return head
        
        # curr = head
        # prev = None

        # for _ in range(k):
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        
        # head.next = self.reverseKGroup(curr, k)

        # return prev
    
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
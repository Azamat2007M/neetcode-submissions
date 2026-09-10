# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode] ) -> Optional[ListNode]: # carry: int = 0 (for recursion)
        #Iterative method Time: O(max(n, m)) Space: O(max(n, m))
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        #Iterative method Time: O(max(n, m)) Space: O(max(n, m))
        # if not l1 and not l2 and carry == 0:
        #     return None

        # val1 = l1.val if l1 else 0
        # val2 = l2.val if l2 else 0

        # total = val1 + val2 + carry
        # new_carry = total // 10
        # val = total % 10

        # result = ListNode(val)

        # next_l1 = l1.next if l1 else None
        # next_l2 = l2.next if l2 else None

        # result.next = self.addTwoNumbers(next_l1, next_l2, new_carry)

        # return result
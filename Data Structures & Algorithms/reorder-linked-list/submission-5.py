# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Two Pointers with merging Time: O(n) (n/2 + n/2 + n/2) Space: O(1)
        # if not head or not head.next:
        #     return

        # slow, fast = head, head.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # second = slow.next
        # slow.next = None
        # curr = second
        # prev = None

        # while curr:
        #     tmp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = tmp
        
        # second = prev
        # first = head

        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first, second = tmp1, tmp2

        #Recursive method Time: O(n) Space: O(n)
        # self.left = head
        
        # def recurse(right: ListNode) -> bool:
        #     if not right:
        #         return True

        #     should_continue = recurse(right.next)
            
        #     if not should_continue:
        #         return False

        #     if self.left == right or self.left.next == right:
        #         right.next = None
        #         return False

        #     tmp = self.left.next
        #     self.left.next = right
        #     right.next = tmp
        #     self.left = tmp

        #     return True

        # recurse(head)

        #Stack method Time: O(n) Space: O(n)

        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head

        for _ in range(len(stack) // 2):
            top = stack.pop()
            nxt = curr.next

            curr.next = top
            top.next = nxt
            curr = nxt

        curr.next = None
        
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []     

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, i, l = heapq.heappop(min_heap)
            curr.next = l
            curr = curr.next

            if l.next:
                heapq.heappush(min_heap, (l.next.val, i, l.next))
        
        return dummy.next

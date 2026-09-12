import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Divide and conquer iterative method Time: O(nlogk) Space: O(1)
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            min_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                min_list.append(self.mergeTwoLists(l1, l2))

            lists = min_list
        
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next

        #Heap method Time: O(nlogk) Space: O(n)
        # min_heap = []     

        # for i, l in enumerate(lists):
        #     if l:
        #         heapq.heappush(min_heap, (l.val, i, l))
        
        # dummy = ListNode(0)
        # curr = dummy

        # while min_heap:
        #     val, i, l = heapq.heappop(min_heap)
        #     curr.next = l
        #     curr = curr.next

        #     if l.next:
        #         heapq.heappush(min_heap, (l.next.val, i, l.next))
        
        # return dummy.next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS iterative with Stack method Time: O(n) Space: O(h)
        # stack = [(p, q)]

        # while stack:
        #     node1, node2 = stack.pop()

        #     if not node1 and not node2:
        #         continue
            
        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False

        #     stack.append((node1.left, node2.left))
        #     stack.append((node1.right, node2.right))

        # return True

        #DFS recursive method Time: O(n) Space: O(h)
        # if not p and not q:
        #     return True
        
        # if not p or not q or p.val != q.val:
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        #BFS iterative with queue method Time: O(n) Space: O(h)
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue
            
            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #BFS iterative method Time: O(n) Space: O(w)
        count = 0
        queue = deque([(root, root.val)])

        while queue:
            node, max_val = queue.popleft()

            if max_val <= node.val:
                count += 1

            new_max = max(max_val, node.val)

            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))
            
        return count

        #DFS recursive method Time: O(n) Space: O(h)
        # def dfs(node, max_val):
        #     if not node:
        #         return 0

        #     count = 1 if max_val <= node.val else 0
        #     new_val = max(max_val, node.val)

        #     return count + dfs(node.left, new_val) + dfs(node.right, new_val)

        # return dfs(root, root.val)
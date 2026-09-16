# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS iterative method Time: O(n) Space: O(w)
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_group = []

            for _ in range(level_size):
                node = queue.popleft()
                current_group.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_group)

        return result

        #DFS recursive method Time: O(n) Space: O(h)
        # result = []

        # def dfs(node, level):
        #     if not node:
        #         return

        #     if len(result) == level:
        #         result.append([])

        #     result[level].append(node.val)

        #     dfs(node.left, level + 1)
        #     dfs(node.right, level + 1)

        
        # dfs(root, 0)

        # return result
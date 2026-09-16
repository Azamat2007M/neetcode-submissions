# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS iterative method Time: O(n) Space: O(w)
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return result

        #DFS recursive method Time: O(n) Space: O(h)
        # result = []

        # def dfs(node, level):
        #     if not node:
        #         return
        
        #     if level == len(result):
        #         result.append(node.val)
            
        #     dfs(node.right, level + 1)
        #     dfs(node.left, level + 1)

        # dfs(root, 0)
        
        # return result
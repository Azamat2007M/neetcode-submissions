# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            
            leftn = dfs(node.left)
            rightn = dfs(node.right)

            self.res = max(self.res, leftn + rightn)

            return 1 + max(leftn, rightn)

        dfs(root)

        return self.res
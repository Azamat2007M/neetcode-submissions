# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #DFS recursive method Time: O(n) Space: O(h)
        def dfs(node) -> int:
            if not node:
                return 0

            lefth = dfs(node.left)
            if lefth == -1:
                return -1
            
            righth = dfs(node.right)
            if righth == -1:
                return -1

            if abs(lefth - righth) > 1:
                return -1
            
            return 1 + max(lefth, righth)
        
        return dfs(root) != -1
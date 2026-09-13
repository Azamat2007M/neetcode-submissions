# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative + Stack method Time: O(n) Space: O(h)
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]

        #DFS recursive method Time: O(n) Space: O(h)
        # res = []

        # def dfs(node):
        #     if not node:
        #         return 
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        
        # dfs(root)

        # return res
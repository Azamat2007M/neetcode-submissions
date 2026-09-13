# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative + Stack method Time: O(n) Space: O(n)
        stack = []
        res = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
        
        #DFS recursive method Time: O(n) Space: O(h)
        # res = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)

        # dfs(root)

        # return res
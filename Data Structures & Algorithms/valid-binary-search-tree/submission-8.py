# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #DFS itertive method Time: O(n) Space: O(h)
        # stack = []
        # curr = root
        # prev = None

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()

        #     if curr.val <= prev:
        #         return False

        #     prev = curr
        #     curr = curr.right

        # return True

        def dfs(node, low = float('-infinity'), high = float('infinity')):
            # DFS recursive method Time: O(n) Space: O(h)
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root)
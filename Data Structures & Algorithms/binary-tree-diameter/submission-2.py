# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Iterative + Stack method Time: O(n) Space: O(h)
        res = 0
        stack = [root]
        heights = {}

        while stack:
            node = stack[-1]

            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                stack.pop()
                leftn = heights.get(node.left, 0)
                rightn = heights.get(node.right, 0)

                res = max(res, leftn + rightn)

                heights[node] = 1 + max(leftn, rightn)
        
        return res


        #DFS recursive method Time: O(n) Space: O(h)
        # self.res = 0

        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     leftn = dfs(node.left)
        #     rightn = dfs(node.right)

        #     self.res = max(self.res, leftn + rightn)

        #     return 1 + max(leftn, rightn)

        # dfs(root)

        # return self.res
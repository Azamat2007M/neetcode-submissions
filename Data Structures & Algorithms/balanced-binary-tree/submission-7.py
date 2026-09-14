# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #DFS Iterative + Stack method Time: O(n) Space: O(h)
        if not root:
            return True

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
                
                lefth = heights.get(node.left, 0)
                righth = heights.get(node.right, 0)

                if abs(lefth - righth) > 1:
                    return False

                heights[node] = 1 + max(lefth, righth)
            
        return True

        #DFS recursive method Time: O(n) Space: O(h)
        # def dfs(node) -> int:
        #     if not node:
        #         return 0

        #     lefth = dfs(node.left)
        #     if lefth == -1:
        #         return -1
            
        #     righth = dfs(node.right)
        #     if righth == -1:
        #         return -1

        #     if abs(lefth - righth) > 1:
        #         return -1
            
        #     return 1 + max(lefth, righth)
        
        # return dfs(root) != -1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #DFS iterative method Time: O(n) Space: O(n)
        stack = [(root, False)]
        dp = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left_rob, not_left_rob = dp.get(node.left, (0, 0))
                right_rob, not_right_rob = dp.get(node.right, (0, 0))

                rob_this = node.val + not_left_rob + not_right_rob
                not_rob_this = max(left_rob, not_left_rob) + max(right_rob, not_right_rob)
                dp[node] = (rob_this, not_rob_this)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return max(dp[root])

        #DFS recursive method Time: O(n) Space: O(h)
        # def dfs(node):
        #     if not node:
        #         return (0, 0)

        #     left_rob, not_left_rob = dfs(node.left)
        #     right_rob, not_right_rob = dfs(node.right)

        #     rob_this = node.val + not_left_rob + not_right_rob
        #     not_rob_this = max(left_rob, not_left_rob) + max(right_rob, not_right_rob)

        #     return (rob_this, not_rob_this)
        
        # return max(dfs(root))
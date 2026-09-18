# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #DFS recursive method Time: O(n) Space: O(h)
        max_sum = float('-infinity')
        stack = [(root, False)]
        gains = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue
            
            if visited:
                left_gain = max(0, gains.get(node.left, 0))
                right_gain = max(0, gains.get(node.right, 0))

                currenth_path_sum = node.val + left_gain + right_gain
                max_sum = max(max_sum, currenth_path_sum)

                gains[node] = node.val + max(left_gain, right_gain)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return max_sum

        #DFS recursive method Time: O(n) Space: O(h)
        # max_sum = float('-infinity')

        # def dfs(node: TreeNode | None) -> int:
        #     if not node:
        #         return 0
            
        #     nonlocal max_sum

        #     left_gain = max(0, dfs(node.left))
        #     right_gain = max(0, dfs(node.right))

        #     currenth_path_sum = node.val + left_gain + right_gain
        #     max_sum = max(max_sum, currenth_path_sum)

        #     return node.val + max(left_gain, right_gain)

        # dfs(root)
        # return max_sum
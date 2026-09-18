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

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            nonlocal max_sum

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            currenth_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, currenth_path_sum)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum
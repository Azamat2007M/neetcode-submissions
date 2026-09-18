# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_id = 0

        
        def dfs(left, right):
            if left > right:
                return

            nonlocal preorder_id

            node_val = preorder[preorder_id]
            node = TreeNode(node_val)
            preorder_id += 1

            mid = inorder_map[node_val]
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            return node

        return dfs(0, len(inorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS iterative method Time: O(n) Space: O(n)
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_id = 0

        for i in range(1, len(inorder)):
            val = preorder[i]
            node = stack[-1]

            if node.val != inorder[inorder_id]:
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_id]:
                    node = stack.pop()
                    inorder_id += 1
                
                node.right = TreeNode(val)
                stack.append(node.right)

        return root

        # DFS recursive method Time: O(n) Space: O(n)
        # inorder_map = {val: i for i, val in enumerate(inorder)}
        # preorder_id = 0

        # def dfs(left, right):
        #     if left > right:
        #         return

        #     nonlocal preorder_id

        #     node_val = preorder[preorder_id]
        #     node = TreeNode(node_val)
        #     preorder_id += 1

        #     mid = inorder_map[node_val]
        #     node.left = dfs(left, mid - 1)
        #     node.right = dfs(mid + 1, right)

        #     return node

        # return dfs(0, len(inorder) - 1)
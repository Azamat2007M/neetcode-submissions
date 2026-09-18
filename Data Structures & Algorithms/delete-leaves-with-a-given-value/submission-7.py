# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #DFS iterative method Time: O(n) Space: O(h)
        if not root:
            return None

        stack = [(root, False)]
        parent = {root: None}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                if not node.left and not node.right and node.val == target:
                    parent_node = parent[node]

                    if not parent_node:
                        return None

                    if parent_node.left == node:
                        parent_node.left = None
                    elif parent_node.right == node:
                        parent_node.right = None

            else:
                stack.append((node, True))
                if node.right:
                    parent[node.right] = node
                    stack.append((node.right, False))
                if node.left:
                    parent[node.left] = node
                    stack.append((node.left, False))
        
        return root

        #DFS recursive method Time: O(n) Space: O(h)
        # if not root:
        #     return None
        
        # root.left = self.removeLeafNodes(root.left, target)
        # root.right = self.removeLeafNodes(root.right, target)

        # if not root.left and not root.right and root.val == target:
        #     return None
        
        # return root
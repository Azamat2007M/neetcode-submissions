# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #DFS itertive method Time: O(h) Space: O(1)
        curr, parent = root, None

        while curr and curr.val != key:
            parent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            
        if not curr:
            return root
        
        if not curr.left:
            new_node = curr.right
        elif not curr.right:
            new_node = curr.left
        else:
            nxt = curr.right

            while nxt.left:
                nxt = nxt.left
            
            nxt.left = curr.left
            new_node = curr.right
        
        if not parent:
            return new_node
        if parent.left == curr:
            parent.left = new_node
        else:
            parent.right = new_node

        return root

        #DFS recursive method Time: O(h) Space: O(h)
        # if not root:
        #     return

        # if root.val > key:
        #     root.left = self.deleteNode(root.left, key)
        # elif root.val < key:
        #     root.right = self.deleteNode(root. right, key)
        # else:
        #     if not root.right:
        #         return root.left
        #     if not root.left:
        #         return root.right

        #     curr = root.right

        #     while curr.left:
        #         curr = curr.left
            
        #     curr.left = root.left
            
        #     return root.right
        
        # return root
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Serializing method Time: O(n + m) Space: O(n + m)
        def serialize(node):
            if not node:
                return ',#'
            
            return f',{node.val}' + serialize(node.left) + serialize(node.right)

        s_root = serialize(root)
        s_subroot = serialize(subRoot)

        return s_subroot in s_root
        #DFS iterative method Time: O(n) Space: O(hr + hs)
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     stack = [root]

    #     while stack:
    #         node = stack.pop()

    #         if node.val == subRoot.val:
    #             if self.isSameTree(node, subRoot):
    #                 return True
            
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)

    #     return False

    
    # def isSameTree(self, t1, t2):
    #     stack = [(t1, t2)]

    #     while stack:
    #         n1, n2 = stack.pop()
            
    #         if not n1 and not n2:
    #             continue
                
    #         if not n1 or not n2 or n1.val != n2.val:
    #             return False
            
    #         stack.append((n1.right, n2.right))
    #         stack.append((n1.left, n2.left))

        
    #     return True

        #DFS recursive method Time: O(n) Space: O(h) 
    #     if not subRoot:
    #         return True
        
    #     if not root:
    #         return False

    #     if self.isSameTree(root, subRoot):
    #         return True

    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # def isSameTree(self, root, subroot):
    #     if not root and not subroot:
    #         return True
        
    #     if not root or not subroot or root.val != subroot.val:
    #         return False
        
    #     return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right)

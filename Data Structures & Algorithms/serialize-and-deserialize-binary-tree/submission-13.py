# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    #BFS method with queue
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('N')
        
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        calls = data.split(',')
        root = TreeNode(int(calls[0]))
        queue = deque([root])
        idx = 1

        while queue and idx < len(calls):
            node = queue.popleft()

            if calls[idx] != 'N':
                node.left = TreeNode(int(calls[idx]))
                queue.append(node.left)

            idx += 1

            if calls[idx] != 'N':
                node.right = TreeNode(int(calls[idx]))
                queue.append(node.right)

            idx += 1

        return root

    # #DFS recursive method 
    # # Encodes a tree to a single string.
    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     res = []

    #     def dfs(node):
    #         if not node:
    #             res.append('N')
    #             return
            
    #         res.append(str(node.val))
    #         dfs(node.left)
    #         dfs(node.right)

    #     dfs(root)
    #     return ','.join(res)
        
    # # Decodes your encoded data to tree.
    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     calls = data.split(',')
    #     self.idx = 0
    #     def dfs():
    #         if calls[self.idx] == 'N':
    #             self.idx += 1
    #             return None
            
    #         node = TreeNode(int(calls[self.idx]))
    #         self.idx += 1
    #         node.left = dfs()
    #         node.right = dfs()

    #         return node

    #     return dfs()
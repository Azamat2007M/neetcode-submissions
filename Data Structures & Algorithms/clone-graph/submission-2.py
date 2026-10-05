"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #DFS recursive method Time: O(v + e) Space: O(v)
        # if not node:
        #     return None

        # old_to_new = {}

        # def dfs(curr):
        #     if curr in old_to_new:
        #         return old_to_new[curr]

        #     copy = Node(curr.val)
        #     old_to_new[curr] = copy

        #     for neighbor in curr.neighbors:
        #         copy.neighbors.append(dfs(neighbor))

        #     return copy

        # return dfs(node)

        #BFS method Time: O(v + e) Space: O(v)
        if not node:
            return None

        old_to_new = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]

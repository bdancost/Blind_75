from typing import Optional, List


# Definition for a Node in a Graph.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Hash Map to map old_node -> new_cloned_node
        old_to_new = {}

        def dfs(current_node: Optional[Node]) -> Optional[Node]:
            if not current_node:
                return None

            # If we already cloned this node, just return its clone from the map
            if current_node in old_to_new:
                return old_to_new[current_node]

            # Create a deep copy of the current node (without neighbors for now)
            copy = Node(current_node.val)
            old_to_new[current_node] = copy

            # Recursively clone all neighbors and attach them to our copy
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


# --- TEST CODE ---
# Creating a simple graph: 1 <-> 2
node1 = Node(1)
node2 = Node(2)
node1.neighbors.append(node2)
node2.neighbors.append(node1)

validator = Solution()
cloned_root = validator.cloneGraph(node1)

print(f"Original Node 1 address: {hex(id(node1))}")
print(f"Cloned Node 1 address:   {hex(id(cloned_root))}")
print(f"Cloned Node 1 Val: {cloned_root.val}, Has neighbor? {cloned_root.neighbors[0].val == 2}")
# The memory addresses must be completely different!
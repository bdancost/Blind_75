from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        # Initialize the queue with the root node
        queue = deque([root])

        # While there are nodes left to process in the tree
        while queue:
            level_size = len(queue)
            current_level = []

            # Process all nodes that belong to the current level
            for _ in range(level_size):
                # Pop the node from the front of the queue (O(1) operation)
                node = queue.popleft()
                current_level.append(node.val)

                # Enqueue the left child if it exists
                if node.left:
                    queue.append(node.left)
                # Enqueue the right child if it exists
                if node.right:
                    queue.append(node.right)

            # Add the completed level to our final results list
            result.append(current_level)

        return result


# --- TEST CODE ---
# Building the tree from the example:
#      3
#     / \
#    9  20
#      /  \
#     15   7
root_node = TreeNode(3)
root_node.left = TreeNode(9)
root_node.right = TreeNode(20, TreeNode(15), TreeNode(7))

validator = Solution()
levels = validator.levelOrder(root_node)

print(f"Tree Level Order Traversal:\n{levels}")
# Should output: [[3], [9, 20], [15, 7]]
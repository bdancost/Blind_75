from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: If the node is null, the depth here is 0
        if not root:
            return 0

        # Step 1: Recursively find the depth of both subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Step 2: The depth of the current node is the maximum between
        # left and right subtrees, plus 1 for the current node itself
        return max(left_depth, right_depth) + 1


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
height = validator.maxDepth(root_node)

print(f"The maximum depth of the binary tree is: {height}")
# Should output: 3
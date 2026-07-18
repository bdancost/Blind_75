from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function that carries the valid range down the tree
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # Base Case: An empty tree or leaf endpoint is always a valid BST
            if not node:
                return True

            # Current node value must be strictly within the low and high boundaries
            if not (low < node.val < high):
                return False

            # Recursively check the subtrees with updated constraints:
            # - Left child must be smaller than current node.val (updates high bound)
            # - Right child must be larger than current node.val (updates low bound)
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Initialize the validation with global boundaries of negative and positive infinity
        return validate(root, float('-inf'), float('inf'))


# --- TEST CODE ---
# Building an INVALID BST example:
#      5
#     / \
#    1   4
#       / \
#      3   6
node_4 = TreeNode(4, TreeNode(3), TreeNode(6))
invalid_root = TreeNode(5, TreeNode(1), node_4)

validator = Solution()
result = validator.isValidBST(invalid_root)

print(f"Is this binary tree a valid BST? {result}")
# Should output: False
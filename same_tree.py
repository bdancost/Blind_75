from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are null, so they are identical
        if not p and not q:
            return True

        # Base Case 2: One of the nodes is null and the other is not (structural mismatch)
        if not p or not q:
            return False

        # Base Case 3: The values of the current nodes do not match
        if p.val != q.val:
            return False

        # If the current nodes are identical, recursively check their left and right subtrees
        # Both left and right subtrees must be identical (using the AND operator)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# --- TEST CODE ---
# Building Tree P: 1 -> left: 2, right: 3
tree_p = TreeNode(1, TreeNode(2), TreeNode(3))

# Building Tree Q: 1 -> left: 2, right: 3
tree_q = TreeNode(1, TreeNode(2), TreeNode(3))

validator = Solution()
is_identical = validator.isSameTree(tree_p, tree_q)

print(f"Are the two binary trees identical? {is_identical}")
# Should output: True
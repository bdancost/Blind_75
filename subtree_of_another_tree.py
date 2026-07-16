from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it cannot contain any subtree
        if not root:
            return False

        # If the tree starting at current 'root' is identical to 'subRoot'
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, recursively search in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function from Day 21 to check structural identity
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# --- TEST CODE ---
# Building Main Tree:
#      3
#     / \
#    4   5
#   / \
#  1   2
sub_left = TreeNode(4, TreeNode(1), TreeNode(2))
main_root = TreeNode(3, sub_left, TreeNode(5))

# Building SubTree:
#    4
#   / \
#  1   2
sub_root = TreeNode(4, TreeNode(1), TreeNode(2))

validator = Solution()
result = validator.isSubtree(main_root, sub_root)

print(f"Is subRoot a subtree of main_root? {result}")
# Should output: True
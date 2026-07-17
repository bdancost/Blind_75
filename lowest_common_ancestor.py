from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current:
            # Case 1: Both nodes are larger than the current node, search in the right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # Case 2: Both nodes are smaller than the current node, search in the left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # Case 3: We found the split point (or one of the nodes is the current node)
            else:
                return current


# --- TEST CODE ---
# Building BST from the example:
#               6
#             /   \
#            2     8
#           / \   / \
#          0   4 7   9
node_4 = TreeNode(4)
node_2 = TreeNode(2, TreeNode(0), node_4)
node_8 = TreeNode(8, TreeNode(7), TreeNode(9))
root_node = TreeNode(6, node_2, node_8)

validator = Solution()
# Let's find the LCA between node 2 and node 8
result = validator.lowestCommonAncestor(root_node, node_2, node_8)

print(f"The Lowest Common Ancestor between {node_2.val} and {node_8.val} is: {result.val}")
# Should output: 6
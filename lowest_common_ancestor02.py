from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # Se ambos os nós estiverem à direita, o LCA está à direita
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Se ambos os nós estiverem à esquerda, o LCA está à esquerda
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Se dividiram caminhos (um à esquerda, um à direita), achamos o LCA!
            else:
                return curr
        return None


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        curr = queue.pop(0)
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1
    return root


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Auxiliar para encontrar a referência do objeto TreeNode pelo valor."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


validator = Solution()

# Montando a BST: [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
bst_root = build_tree_level_order([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

# Teste 1: LCA de 2 e 8 -> Deve ser 6
node_p1 = find_node(bst_root, 2)
node_q1 = find_node(bst_root, 8)
lca1 = validator.lowestCommonAncestor(bst_root, node_p1, node_q1)
print(f"LCA de 2 e 8: {lca1.val}")  # 6

# Teste 2: LCA de 2 e 4 -> Deve ser 2
node_p2 = find_node(bst_root, 2)
node_q2 = find_node(bst_root, 4)
lca2 = validator.lowestCommonAncestor(bst_root, node_p2, node_q2)
print(f"LCA de 2 e 4: {lca2.val}")  # 2
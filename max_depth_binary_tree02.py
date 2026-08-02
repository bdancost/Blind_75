from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Caso base: árvore/nó vazio tem profundidade 0
        if not root:
            return 0

        # Profundidade das subárvores esquerda e direita
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # A altura atual é 1 (o próprio nó) + o máximo entre as duas subárvores
        return 1 + max(left_depth, right_depth)


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


validator = Solution()

# Teste 1: [3, 9, 20, None, None, 15, 7] -> Deve retornar 3
tree1 = build_tree_level_order([3, 9, 20, None, None, 15, 7])
print(f"Profundidade Máxima (Teste 1): {validator.maxDepth(tree1)}")  # 3

# Teste 2: [1, None, 2] -> Deve retornar 2
tree2 = build_tree_level_order([1, None, 2])
print(f"Profundidade Máxima (Teste 2): {validator.maxDepth(tree2)}")  # 2
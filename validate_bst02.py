from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
            # Caso base: nó nulo é considerado válido
            if not node:
                return True

            # Se o nó violar o intervalo permitido (low < val < high)
            if node.val <= low or node.val >= high:
                return False

            # Valida recursivamente a subárvore esquerda e a direita ajustando os limites
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)


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

# Teste 1: BST Válida [2, 1, 3] -> Deve retornar True
tree1 = build_tree_level_order([2, 1, 3])
print(f"Teste 1 (Válida): {validator.isValidBST(tree1)}")  # True

# Teste 2: BST Inválida [5, 1, 4, None, None, 3, 6] -> Deve retornar False
tree2 = build_tree_level_order([5, 1, 4, None, None, 3, 6])
print(f"Teste 2 (Inválida): {validator.isValidBST(tree2)}")  # False
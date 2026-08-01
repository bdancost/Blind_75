from typing import Optional, List


# Definição de um Nó de Árvore Binária (padrão do LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Caso base: Se a árvore/nó for vazia, retorna None
        if not root:
            return None

        # Troca os ponteiros da esquerda e da direita (Padrão Pythonico)
        root.left, root.right = root.right, root.left

        # Chama a função recursivamente para as duas subárvores
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Retorna a raiz da árvore já invertida
        return root


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Cria uma Árvore Binária a partir de uma lista em nível."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        curr = queue.pop(0)

        # Filho Esquerdo
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1

        # Filho Direito
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converte a Árvore de volta para Lista em Nível para facilitar a impressão."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Limpa os 'None' do final da representação
    while result and result[-1] is None:
        result.pop()
    return result


validator = Solution()

# Teste: Inverter [4, 2, 7, 1, 3, 6, 9]
tree_root = build_tree_level_order([4, 2, 7, 1, 3, 6, 9])
inverted = validator.invertTree(tree_root)

print("Árvore Invertida em Nível:")
print(tree_to_list(inverted))
# Deve imprimir: [4, 7, 2, 9, 6, 3, 1]
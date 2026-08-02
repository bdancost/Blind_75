from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        # Fila para controlar a travessia em largura (BFS)
        queue = deque([root])

        while queue:
            level_size = len(queue)  # Quantidade de nós no nível atual
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Adiciona os filhos na fila para serem processados no próximo nível
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        curr = q.popleft()
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            q.append(curr.left)
        i += 1
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            q.append(curr.right)
        i += 1
    return root


validator = Solution()

# Teste: [3, 9, 20, None, None, 15, 7]
tree = build_tree_level_order([3, 9, 20, None, None, 15, 7])
res = validator.levelOrder(tree)

print(f"Travessia por níveis: {res}")
# Deve imprimir: [[3], [9, 20], [15, 7]]
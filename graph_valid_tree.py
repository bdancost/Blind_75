from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Regra de Ouro: Uma árvore com 'n' nós DEVE ter exatamente 'n - 1' arestas
        if len(edges) != n - 1:
            return False

        # Passo 1: Montar a Lista de Adjacência (Dicionário de Vizinhos)
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        # Passo 2: DFS para verificar ciclos
        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False  # Encontrou um ciclo!

            visited.add(node)

            for neighbor in adj[node]:
                # Ignora o nó de onde acabamos de vir (não é ciclo voltar pro pai)
                if neighbor == parent:
                    continue
                # Se encontrar um ciclo na subárvore, repassa o False
                if not dfs(neighbor, node):
                    return False

            return True

        # Inicia a DFS a partir do nó 0 (passando parent = -1)
        if not dfs(0, -1):
            return False

        # Passo 3: Garante que todos os 'n' nós foram alcançados (Grafo Conectado)
        return len(visited) == n


# --- CÓDIGO DE TESTE ---
validator = Solution()

# Exemplo válido (5 nós, 4 arestas)
print("Teste 1 (Árvore Válida):", validator.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # True

# Exemplo inválido (contém ciclo 1-2-3-1)
print("Teste 2 (Com Ciclo):", validator.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # False
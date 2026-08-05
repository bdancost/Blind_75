from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0

        # 1. Encontra todas as laranjas podres iniciais e conta as frescas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Caso especial: se não houver laranjas frescas desde o início
        if fresh_count == 0:
            return 0

        # Direções para navegar na grade (cima, baixo, esquerda, direita)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 2. Multi-Source BFS
        while queue and fresh_count > 0:
            minutes += 1
            # Processa todas as laranjas podres do minuto atual em lote
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Se a célula vizinha for válida e contiver uma laranja fresca
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Fica podre
                        fresh_count -= 1
                        queue.append((nr, nc))

        # Se ainda sobrou alguma laranja fresca que não pôde ser alcançada
        return minutes if fresh_count == 0 else -1


# =====================================================================
# --- TESTES ---
# =====================================================================

validator = Solution()

# Teste 1: Caso normal -> Deve levar 4 minutos
grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(f"Minutos necessários (Teste 1): {validator.orangesRotting(grid1)}")  # 4

# Teste 2: Laranja isolada -> Impossível apodrecer todas -> Deve retornar -1
grid2 = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
print(f"Minutos necessários (Teste 2): {validator.orangesRotting(grid2)}")  # -1
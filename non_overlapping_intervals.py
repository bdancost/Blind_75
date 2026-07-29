from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Passo 1: Ordenar os intervalos pelo horário de TÉRMINO (índice 1)
        # Quem termina mais cedo ganha prioridade de ficar no calendário!
        intervals.sort(key=lambda x: x[1])

        removals = 0
        # Guarda o horário de término do primeiro intervalo mantido
        prev_end = intervals[0][1]

        # Passo 2: Percorrer a partir do segundo intervalo
        for current in intervals[1:]:
            current_start, current_end = current[0], current[1]

            # Se o início atual for menor que o término anterior, HÁ CONFLITO!
            if current_start < prev_end:
                # Decisão gananciosa: "Removemos" o intervalo atual para manter o menor término
                removals += 1
            else:
                # Sem conflito: Mantemos o intervalo e atualizamos a borda de término
                prev_end = current_end

        return removals


# --- CÓDIGO DE TESTE ---
validator = Solution()

test_intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
res = validator.eraseOverlapIntervals(test_intervals)

print(f"Mínimo de intervalos para remover: {res}")
# Deve retornar: 1
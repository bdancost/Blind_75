from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # FASE 1: Adiciona todos os intervalos que terminam ANTES de newInterval começar
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # FASE 2: Enquanto houver sobreposição, expande e funde o newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Adiciona o novo intervalo já fundido na posição correta
        result.append(newInterval)

        # FASE 3: Adiciona todos os intervalos restantes que ficam DEPOIS
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# --- CÓDIGO DE TESTE ---
validator = Solution()

test_intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_item = [4, 8]

res = validator.insert(test_intervals, new_item)

print(f"Resultado final após inserção: {res}")
# Deve retornar: [[1, 2], [3, 10], [12, 16]]
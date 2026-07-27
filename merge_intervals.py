from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Passo 1: Ordenar os intervalos pelo valor do início (índice 0)
        # Exemplo: [[8,10], [1,3], [2,6]] vira [[1,3], [2,6], [8,10]]
        intervals.sort(key=lambda x: x[0])

        # Passo 2: Inicializar o resultado com o primeiro intervalo
        merged = [intervals[0]]

        # Passo 3: Percorrer os demais intervalos a partir do segundo
        for current in intervals[1:]:
            last_merged = merged[-1]

            # Se o início do intervalo atual é <= ao fim do último intervalo salvo
            if current[0] <= last_merged[1]:
                # Há sobreposição! Atualizamos o fim do último intervalo salvo
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # Não há sobreposição, adiciona o novo intervalo ao resultado
                merged.append(current)

        return merged


# --- CÓDIGO DE TESTE ---
validator = Solution()

test_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
res = validator.merge(test_intervals)

print(f"Intervalos fundidos: {res}")
# Deve retornar: [[1, 6], [8, 10], [15, 18]]
import heapq


class MedianFinder:

    def __init__(self):
        # Max-Heap para a metade dos números MENORES (multiplicamos por -1 para simular Max-Heap)
        self.small_heap = []
        # Min-Heap para a metade dos números MAIORES
        self.large_heap = []

    def addNum(self, num: int) -> None:
        # 1. Por padrão, adicionamos no Max-Heap (metade dos menores)
        heapq.heappush(self.small_heap, -1 * num)

        # 2. Garantir a ordem: o maior do small_heap DEVE ser <= ao menor do large_heap
        if (self.small_heap and self.large_heap and
                (-1 * self.small_heap[0]) > self.large_heap[0]):
            # Remove o maior do small e joga no large
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)

        # 3. Garantir o balanceamento de tamanho (diferença máxima de 1 elemento)
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)

        if len(self.large_heap) > len(self.small_heap) + 1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * val)

    def findMedian(self) -> float:
        # Se um heap tem mais elementos, o topo dele é a mediana
        if len(self.small_heap) > len(self.large_heap):
            return float(-1 * self.small_heap[0])
        if len(self.large_heap) > len(self.small_heap):
            return float(self.large_heap[0])

        # Se os dois têm o mesmo tamanho, faz a média dos dois topos
        return (-1 * self.small_heap[0] + self.large_heap[0]) / 2.0


# --- CÓDIGO DE TESTE ---
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(f"Mediana de [1, 2]: {mf.findMedian()}")  # Esperado: 1.5

mf.addNum(3)
print(f"Mediana de [1, 2, 3]: {mf.findMedian()}")  # Esperado: 2.0
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # 1. Coloca o primeiro nó de cada uma das k listas no Min-Heap
        for i, l in enumerate(lists):
            if l:
                # Tupla: (valor do nó, índice de origem, nó)
                heapq.heappush(heap, (l.val, i, l))

        dummy = ListNode()
        curr = dummy

        # 2. Processa o menor elemento do heap por vez
        while heap:
            val, i, node = heapq.heappop(heap)

            # Anexa o menor nó à lista resultante
            curr.next = node
            curr = curr.next

            # Se houver um próximo nó nessa mesma lista, adiciona no heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


validator = Solution()

# Teste 1: [1->4->5, 1->3->4, 2->6] -> Deve retornar [1, 1, 2, 3, 4, 4, 5, 6]
l1 = build_linked_list([1, 4, 5])
l2 = build_linked_list([1, 3, 4])
l3 = build_linked_list([2, 6])

merged = validator.mergeKLists([l1, l2, l3])
print(f"Resultado Teste 1: {linked_list_to_list(merged)}")
# [1, 1, 2, 3, 4, 4, 5, 6]
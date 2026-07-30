from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Enquanto o ponteiro rápido 'fast' e o seu próximo nó 'fast.next' existirem
        while fast and fast.next:
            slow = slow.next  # Anda 1 passo
            fast = fast.next.next  # Anda 2 passos

            # Se os dois ponteiros se encontrarem no mesmo nó de memória, existe um ciclo!
            if slow == fast:
                return True

        # Se o 'fast' chegou no final da lista (None), não existe ciclo!
        return False


# =====================================================================
# --- CÓDIGO DE TESTE COM CRIADOR DE CICLO ---
# =====================================================================

def build_linked_list_with_cycle(elements: List[int], pos: int) -> Optional[ListNode]:
    """Cria uma lista encadeada e conecta o último nó ao nó do índice 'pos' para criar um ciclo."""
    if not elements:
        return None

    nodes = [ListNode(val) for val in elements]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Se 'pos' for um índice válido, conecta o último nó de volta ao nó 'pos'
    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


validator = Solution()

# Teste 1: Lista COM ciclo (O último nó '4' aponta de volta para o nó '2' no índice 1)
head_com_ciclo = build_linked_list_with_cycle([3, 2, 0, -4], pos=1)
print(f"Teste 1 (Com ciclo): {validator.hasCycle(head_com_ciclo)}")  # Esperado: True

# Teste 2: Lista SEM ciclo
head_sem_ciclo = build_linked_list_with_cycle([1, 2, 3, 4], pos=-1)
print(f"Teste 2 (Sem ciclo): {validator.hasCycle(head_sem_ciclo)}")  # Esperado: False
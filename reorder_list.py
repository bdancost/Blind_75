from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Modifica a lista in-place e não retorna nada.
        """
        if not head or not head.next:
            return

        # PASSO 1: Encontrar o meio da lista (Ponteiros Lento e Rápido)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # PASSO 2: Inverter a segunda metade da lista
        # 'slow.next' é o início da segunda metade
        second = slow.next
        slow.next = None  # Corta a conexão entre a primeira e a segunda metade

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # 'prev' agora é a cabeça da segunda metade invertida

        # PASSO 3: Intercalar (Merge) as duas metades (first e prev)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

def build_linked_list(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    head = ListNode(elements[0])
    curr = head
    for val in elements[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_linked_list(head: Optional[ListNode]) -> None:
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(result) + " -> None")


validator = Solution()

# Teste 1: [1, 2, 3, 4, 5] -> Deve virar [1, 5, 2, 4, 3]
head1 = build_linked_list([1, 2, 3, 4, 5])
validator.reorderList(head1)
print("Resultado Teste 1:")
print_linked_list(head1)

# Teste 2: [1, 2, 3, 4] -> Deve virar [1, 4, 2, 3]
head2 = build_linked_list([1, 2, 3, 4])
validator.reorderList(head2)
print("Resultado Teste 2:")
print_linked_list(head2)
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Criamos o nó Dummy para lidar com a remoção da própria cabeça com segurança
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 1. Avança o ponteiro 'right' em 'n' posições à frente
        for _ in range(n):
            right = right.next

        # 2. Move ambos os ponteiros até que 'right' alcance o final (None)
        while right:
            left = left.next
            right = right.next

        # 3. 'left' está agora no nó anterior ao que deve ser removido.
        # Ajusta o ponteiro 'next' para pular o nó alvo (deletando-o)
        left.next = left.next.next

        # Retorna a verdadeira cabeça da lista ajustada
        return dummy.next


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

# Teste 1: Remover o 2º a partir do fim de [1, 2, 3, 4, 5] (deve remover o 4)
lista1 = build_linked_list([1, 2, 3, 4, 5])
head1 = validator.removeNthFromEnd(lista1, 2)
print("Resultado Teste 1:")
print_linked_list(head1)  # Esperado: 1 -> 2 -> 3 -> 5 -> None

# Teste 2: Remover o 1º a partir do fim (cabeça) em lista de 1 elemento [1]
lista2 = build_linked_list([1])
head2 = validator.removeNthFromEnd(lista2, 1)
print("Resultado Teste 2:")
print_linked_list(head2)  # Esperado: None
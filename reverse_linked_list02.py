from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# =====================================================================
# 💡 FUNÇÕES UTILITÁRIAS PARA FACILITAR OS SEUS TESTES
# =====================================================================

def build_linked_list(elements: List[int]) -> Optional[ListNode]:
    """Converte um Array comum [1, 2, 3...] em uma Linked List automaticamente."""
    if not elements:
        return None

    head = ListNode(elements[0])
    curr = head
    for val in elements[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(head: Optional[ListNode]) -> None:
    """Imprime a Linked List de forma legível no terminal."""
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(result) + " -> None")


# =====================================================================
# --- CÓDIGO DE TESTE AGORA SUPER SIMPLES ---
# =====================================================================

# 1. Passe qualquer lista gigante do Python diretamente aqui:
dados_de_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Converte para Linked List em uma linha
minha_lista = build_linked_list(dados_de_teste)

# 3. Executa a inversão
validator = Solution()
lista_invertida = validator.reverseList(minha_lista)

# 4. Imprime o resultado
print("Lista Invertida:")
print_linked_list(lista_invertida)
# Saída: 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Nó fictício (Dummy) para simplificar a construção da lista
        dummy = ListNode(0)
        tail = dummy

        # Enquanto houver elementos em ambas as listas
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Engata o restante da lista que sobrou (se houver)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Retorna a cabeça da nova lista (ignorando o nó dummy inicial)
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

# Instanciando as duas listas ordenadas
l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])

# Executando o Merge
merged_head = validator.mergeTwoLists(l1, l2)

print("Resultado do Merge:")
print_linked_list(merged_head)
# Deve imprimir: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
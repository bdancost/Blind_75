from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Caso base: se a lista estiver vazia ou com apenas 1 elemento
        if not head or not head.next:
            return head

        # 1. Encontrar o meio da lista (Ponteiro lento e rápido)
        left = head
        right = self._get_mid(head)
        tmp = right.next
        right.next = None  # Corta a conexão entre a primeira e a segunda metade
        right = tmp

        # 2. Recursão (Divisão)
        left = self.sortList(left)
        right = self.sortList(right)

        # 3. Intercalação (Merge de duas listas ordenadas)
        return self._merge(left, right)

    def _get_mid(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Anexa o restante de uma das listas, se houver
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

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

# Teste 1: [4, 2, 1, 3] -> Deve retornar [1, 2, 3, 4]
ll1 = build_linked_list([4, 2, 1, 3])
sorted_ll1 = validator.sortList(ll1)
print(f"Resultado Teste 1: {linked_list_to_list(sorted_ll1)}")  # [1, 2, 3, 4]

# Teste 2: [-1, 5, 3, 4, 0] -> Deve retornar [-1, 0, 3, 5]
ll2 = build_linked_list([-1, 5, 3, 4, 0])
sorted_ll2 = validator.sortList(ll2)
print(f"Resultado Teste 2: {linked_list_to_list(sorted_ll2)}")  # [-1, 0, 3, 5]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        # Percorre enquanto o nó atual e o próximo existirem
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Pula o nó duplicado
                curr.next = curr.next.next
            else:
                # Avança para o próximo nó apenas se não houver duplicação
                curr = curr.next

        return head


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


validator = Solution()

# Teste 1: [1, 1, 2] -> Deve virar [1, 2]
ll1 = build_linked_list([1, 1, 2])
res1 = validator.deleteDuplicates(ll1)
print(f"Teste 1: {linked_list_to_list(res1)}")  # [1, 2]

# Teste 2: [1, 1, 2, 3, 3] -> Deve virar [1, 2, 3]
ll2 = build_linked_list([1, 1, 2, 3, 3])
res2 = validator.deleteDuplicates(ll2)
print(f"Teste 2: {linked_list_to_list(res2)}")  # [1, 2, 3]
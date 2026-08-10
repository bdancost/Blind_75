from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head

        # 1. Copia todos os valores da Linked List para uma lista Python
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # 2. Valida se o array é palíndromo usando 2 ponteiros
        left, right = 0, len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1

        return True


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


validator = Solution()

# Teste 1: [1, 2, 2, 1] -> Deve retornar True
ll1 = build_linked_list([1, 2, 2, 1])
print(f"Teste 1: {validator.isPalindrome(ll1)}")  # True

# Teste 2: [1, 2] -> Deve retornar False
ll2 = build_linked_list([1, 2])
print(f"Teste 2: {validator.isPalindrome(ll2)}")  # False
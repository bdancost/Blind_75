from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # Percorre até os dois ponteiros se encontrarem
        while pA != pB:
            # Se pA chegar ao fim, vai para a cabeça da Lista B; caso contrário, avança
            pA = pA.next if pA else headB
            # Se pB chegar ao fim, vai para a cabeça da Lista A; caso contrário, avança
            pB = pB.next if pB else headA

        return pA


# =====================================================================
# --- FUNÇÕES UTILITÁRIAS E TESTES ---
# =====================================================================

validator = Solution()

# Teste 1: Criando duas listas com interseção no nó 'intersect' (valor 8)
intersect = ListNode(8)
intersect.next = ListNode(4)
intersect.next.next = ListNode(5)

# Lista A: 4 -> 1 -> (8 -> 4 -> 5)
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersect

# Lista B: 5 -> 6 -> 1 -> (8 -> 4 -> 5)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersect

res1 = validator.getIntersectionNode(headA, headB)
print(f"Teste 1 (Com Interseção): {res1.val if res1 else 'None'}")  # Deve imprimir: 8

# Teste 2: Duas listas sem interseção
headC = ListNode(1)
headC.next = ListNode(2)

headD = ListNode(3)
headD.next = ListNode(4)

res2 = validator.getIntersectionNode(headC, headD)
print(f"Teste 2 (Sem Interseção): {res2.val if res2 else 'None'}")  # Deve imprimir: None
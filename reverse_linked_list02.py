from typing import Optional


# Definição de um Nó da Lista Encadeada (padrão do LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next  # 1. Guarda a referência do próximo nó
            curr.next = prev  # 2. Inverte o ponteiro (aponta para trás)
            prev = curr  # 3. Move o ponteiro 'prev' um passo à frente
            curr = nxt  # 4. Move o ponteiro 'curr' um passo à frente

        return prev  # 'prev' agora é a nova cabeça da lista invertida


# --- CÓDIGO DE TESTE E MONTAGEM DA LISTA ---
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

validator = Solution()
new_head = validator.reverseList(node1)

# Imprimindo a lista invertida para validar
result = []
temp = new_head
while temp:
    result.append(str(temp.val))
    temp = temp.next

print("Lista Invertida: " + " -> ".join(result) + " -> None")

from typing import Optional


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next = next_node


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the previous pointer as None, because the new tail will point to None
        prev = None
        current = head

        while current:
            # 1. Temporarily store the next node
            next_node = current.next

            # 2. Reverse the link (the actual magic happens here)
            current.next = prev

            # 3. Move the pointers one step forward for the next iteration
            prev = current
            current = next_node

        # At the end, 'prev' will be pointing to the new head of the reversed list
        return prev


# --- TEST CODE ---
# Creating a linked list: 1 -> 2 -> 3 -> None
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

validator = Solution()
reversed_head = validator.reverseList(node1)

# Printing the reversed list to verify: should display 3 -> 2 -> 1 -> None
output = []
current_print = reversed_head
while current_print:
    output.append(str(current_print.val))
    current_print = current_print.next
print("Reversed List:", " -> ".join(output) + " -> None")
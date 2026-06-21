from typing import Optional


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next = next_node


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to seamlessly handle edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 1: Advance 'right' pointer 'n' steps forward to create the gap
        for _ in range(n):
            if right:
                right = right.next

        # Step 2: Move both pointers until 'right' hits the end of the list
        while right:
            left = left.next
            right = right.next

        # Step 3: Delete the target node by skipping it in the chain
        # left is currently pointing to the node BEFORE the one to be deleted
        if left.next:
            left.next = left.next.next

        # Return the actual head of the modified list
        return dummy.next


# --- TEST CODE ---
# Creating list: 1 -> 2 -> 3 -> 4 -> 5 -> None
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

validator = Solution()
# Let's remove the 2nd node from the end (which is node 4)
new_head = validator.removeNthFromEnd(node1, 2)

# Printing result: should display 1 -> 2 -> 3 -> 5 -> None
output = []
current = new_head
while current:
    output.append(str(current.val))
    current = current.next
print("Modified List:", " -> ".join(output) + " -> None")
from typing import Optional


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next = next_node


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers at the start of the linked list
        slow = head
        fast = head

        # 'fast' moves twice as fast, so we must ensure 'fast' and 'fast.next' exist
        while fast and fast.next:
            slow = slow.next  # Moves 1 step
            fast = fast.next.next  # Moves 2 steps

            # If they meet, there is a cycle (the hare caught up with the tortoise)
            if slow == fast:
                return True

        # If 'fast' reaches the end of the list, there is no cycle
        return False


# --- TEST CODE ---
# Creating a list with a cycle: 1 -> 2 -> 3 -> (points back to 2)
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# Manually creating the cycle: making node3 point back to node2
node3.next = node2

validator = Solution()
result = validator.hasCycle(node1)

print(f"Does the linked list have a cycle? {result}")
# Should output: True
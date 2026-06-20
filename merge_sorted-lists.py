from typing import Optional


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next = next_node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the start anchor of our merged list
        dummy = ListNode()
        tail = dummy

        # 2. Loop while both lists still have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Connect the smaller node to our tail
                list1 = list1.next  # Move pointer in list1 forward
            else:
                tail.next = list2  # Connect the smaller node to our tail
                list2 = list2.next  # Move pointer in list2 forward

            tail = tail.next  # Move the tail pointer forward in our new list

        # 3. If one list is exhausted, append the remaining part of the other list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # The real merged list starts right after the dummy node
        return dummy.next


# --- TEST CODE ---
# Creating list1: 1 -> 2 -> 4 -> None
node_1_4 = ListNode(4)
node_1_2 = ListNode(2, node_1_4)
list1_head = ListNode(1, node_1_2)

# Creating list2: 1 -> 3 -> 4 -> None
node_2_4 = ListNode(4)
node_2_3 = ListNode(3, node_2_4)
list2_head = ListNode(1, node_2_3)

validator = Solution()
merged_head = validator.mergeTwoLists(list1_head, list2_head)

# Printing result: should display 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
output = []
current = merged_head
while current:
    output.append(str(current.val))
    current = current.next
print("Merged List:", " -> ".join(output) + " -> None")
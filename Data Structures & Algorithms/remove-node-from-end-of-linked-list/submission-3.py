# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time: - Space: -

        newHead = ListNode(None, head)
        first, second = head, newHead
        first_counter, second_counter = 0, -1

        while first:
            if first_counter - second_counter > n:
                second_counter += 1
                second = second.next
            first = first.next
            first_counter += 1
        
        second.next = second.next.next

        return newHead.next
        

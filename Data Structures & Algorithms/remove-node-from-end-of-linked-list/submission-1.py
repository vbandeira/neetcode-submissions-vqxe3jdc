# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time: O(N) Space: O(1)
        
        # Iter over list to get length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        # Initiate a new heaad to handle removing the first element
        newHead = ListNode(None, head)

        # Iter until length - n and update pointer
        curr = newHead
        for _ in range(length - n):
            curr = curr.next
        curr.next = curr.next.next

        return newHead.next
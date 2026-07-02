# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list (will be slow value)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split list in two
        first = head
        second = slow.next # Should be next one
        slow.next = None # Breaks the list in two

        # Reverse l2
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second = prev

        # Build result
        while first and second:
            tmp_first = first.next
            tmp_second = second.next
            first.next = second
            second.next = tmp_first
            first = tmp_first
            second = tmp_second            

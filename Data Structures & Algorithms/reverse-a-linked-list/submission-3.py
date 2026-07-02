# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mode = 'iter'
        if mode == 'rec':
            # Recursive: Time: O(N), Space: O(N)
            if not head: return None

            newHead = head
            if head.next:
                newHead = self.reverseList(head.next)
                head.next.next = head
            head.next = None
            return newHead
        
        # Iterative: Two pointers (Prev e Curr) - Time: O(N) Space: O(1)
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
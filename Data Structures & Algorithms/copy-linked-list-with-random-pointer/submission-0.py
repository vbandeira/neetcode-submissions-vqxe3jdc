"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        - Lista contem o valor e o índice para o random;
        - Iterar sobre head recriando a nova lista sem conexões;
        - Hashmap com o apontamento do nó original para a cópia;
        - Iterar novamente atualizando nova lista usando os apontamentos;
        '''

        node_map = {None: None}
        curr = head

        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        new_head = node_map[head]
        # new_curr = new_head
        # curr = head.next
        curr = head
        while curr:
            # new_curr.next = node_map[curr.next]
            # new_curr.random = node_map[curr.random]
            # curr = curr.next
            # new_curr = new_curr.next
            copy = node_map[curr]
            copy.next = node_map[curr.next]
            copy.random = node_map[curr.random]
            curr = curr.next

        return new_head

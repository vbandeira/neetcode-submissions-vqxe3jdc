class LRUCache:

    class ListNode:
        def __init__(self, key = None, value = None, prev_node = None, next_node = None):
            self.key = key
            self.value = value
            self.prev_node = prev_node
            self.next_node = next_node
        
        def __repr__(self):
            return ' - '.join([str(self.key), str(self.value), str(self.next_node.value if self.next_node else '')])

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Linked List with Hashmap for faster access
        self.cache = {}
        self.head = self.ListNode()  # Dummy Node
        self.tail = self.ListNode()  # Another one
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
    
    def _remove(self, node: ListNode):
        prv, nxt = node.prev_node, node.next_node
        prv.next_node, nxt.prev_node = nxt, prv
    
    def _insert(self, node: ListNode):
        prv, nxt = self.tail.prev_node, self.tail
        prv.next_node = nxt.prev_node = node
        node.next_node, node.prev_node = nxt, prv

    def get(self, key: int) -> int:
        # Look in hashmap for key
        # If found, node for key becomes next for tail
        # Return its value
        # Else return -1
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        curr = None
        
        # Look for key and updates or creates it
        if key in self.cache:
            self._remove(self.cache[key])
        
        curr = self.ListNode(key, value)
        self.cache[key] = curr
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Head points to its next
            head_node = self.head.next_node
            self._remove(head_node)
            del self.cache[head_node.key]

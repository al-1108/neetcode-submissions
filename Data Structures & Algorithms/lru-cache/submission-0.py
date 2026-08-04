class Node:
    def __init__(self, key: int, val: int):
        self.val, self.key = val, key
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(0,0), Node(0,0)
        self.tail.next, self.head.prev = self.head, self.tail   
    
    def insert(self, new_node: 'Node'):
        new_node.prev, new_node.next = self.head.prev, self.head
        self.head.prev.next = self.head.prev = new_node

    def remove(self, node):
        node.prev.next, node.next.prev, = node.next, node.prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = new_node = Node(key, value)
        self.insert(new_node)
        if len(self.cache) > self.capacity:
            self.cache.pop(self.tail.next.key)
            self.remove(self.tail.next)

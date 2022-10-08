class DoublyLinkedList:
    def __init__(self, data, next, prev):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"({self.data}) -> {self.next.__repr__()}"

class Cache:

    def __init__(self, capacity):
        self.registry = {}
        self.MRU: DoublyLinkedList = None
        self.LRU: DoublyLinkedList = None
        self.capacity = capacity
        self.usage = 0


    def lookup(self, data):
        if data not in self.registry:
            return None
        else:
            node = self.registry[data]
            if node != self.MRU:
                if node == self.LRU:
                    self.LRU = node.prev
                self.remove_node(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next = self.MRU
        node.prev = None
        self.MRU = node

    def put(self, data):
        if data not in {}:
            if self.usage == self.capacity:
                self.remove_lru()
            new_node = DoublyLinkedList(data, self.MRU, None)
            if self.MRU:
                self.MRU.prev = new_node
            self.registry[data] = new_node
            self.usage += 1
            if not self.LRU:
                self.LRU = self.MRU
            self.MRU = new_node
        else:
            node = self.registry[data]
            if node == self.LRU:
                self.LRU = self.LRU.prev
                self.LRU.next = None
            elif node != self.MRU:
                self.remove_node(node)

    def remove_lru(self):
        node = self.registry.pop(self.LRU.data)
        self.usage -= 1
        if node == self.MRU:
            self.MRU = None
            self.LRU = None
        else:
            node.prev.next = node.next
            self.LRU = node.prev

    def __repr__(self) -> str:
        return f"{self.usage}/{self.capacity}. LRU = {self.LRU}. MRU = {self.MRU} : [{self.registry}]"


cache = Cache(5)
cache.put(1)
cache.put(2)
cache.put(3)
cache.put(4)
cache.put(5)
cache.put(6)
cache.lookup(2)
cache.put(7)
cache.lookup(4)
print(cache)
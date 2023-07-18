class Node():
    def __init__(self, val=0, key=0, next=None, pre=None):
        self.val = val
        self.key = 0
        self.next = next
        self.pre = pre
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node: 
            newNode = Node()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self.add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.move_to_head(node)
        
    def add_node(self, node):
        node.next = self.head.next
        node.pre = self.head
        
        self.head.next.pre = node
        self.head.next = node
    
    def remove_node(self, node):
        pre = node.pre
        new = node.next

        pre.next = new
        new.pre = pre

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        res = self.tail.pre
        self.remove_node(res)
        return res
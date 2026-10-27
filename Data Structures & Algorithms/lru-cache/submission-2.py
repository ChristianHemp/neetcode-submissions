class Node():
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # put accessed node to back of linked list
            curr = self.cache[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


            curr.prev = self.tail.prev
            curr.next = self.tail
            self.tail.prev.next = curr
            self.tail.prev = curr

            return curr.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # put accessed node to back of linked list
            curr = self.cache[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


            curr.prev = self.tail.prev
            curr.next = self.tail
            self.tail.prev.next = curr
            self.tail.prev = curr

            curr.val = value
        else:
            self.cache[key] = Node(key, value)

            if len(self.cache) > self.capacity:
                # remove LRU node
                key_to_remove = self.head.next.key
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.cache[key_to_remove]

                # add new node
                new_node = self.cache[key]
                new_node.prev = self.tail.prev
                new_node.next = self.tail
                self.tail.prev.next = new_node
                self.tail.prev = new_node
            else:
                # add new LRU node
                new_node = self.cache[key]
                new_node.prev = self.tail.prev
                new_node.next = self.tail
                self.tail.prev.next = new_node
                self.tail.prev = new_node
                
        

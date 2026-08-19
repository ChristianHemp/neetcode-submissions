class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        # init doubly linked list w/ dummy nodes
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # update LRU priority
            curr = self.cache[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            curr.prev = self.tail.prev
            curr.prev.next = curr
            self.tail.prev = curr
            curr.next = self.tail

            return curr.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            # update LRU priority
            curr = self.cache[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            curr.prev = self.tail.prev
            curr.prev.next = curr
            self.tail.prev = curr
            curr.next = self.tail
        else:
            self.cache[key] = Node(key, value)

            # cache full
            if len(self.cache) > self.capacity:
                # remove LRU node
                remove_key = self.head.next.key
                curr = self.head.next.next
                self.head.next = curr
                curr.prev = self.head
                del self.cache[remove_key]

                # add new MRU node
                new_node = self.cache[key]
                curr = self.tail.prev
                curr.next = new_node
                new_node.prev = curr
                new_node.next = self.tail
                self.tail.prev = new_node
            # cache not full
            else:
                # add new LRU node
                new_node = self.cache[key]
                curr = self.tail.prev
                curr.next = new_node
                new_node.prev = curr
                new_node.next = self.tail
                self.tail.prev = new_node

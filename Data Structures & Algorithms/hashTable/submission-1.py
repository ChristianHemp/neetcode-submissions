class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:  
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = [None] * capacity
    
    def hash(self, key):
        index = hash(key)

        return index % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            # index is empty, put
            if self.arr[index] == None or self.arr[index].val == "deleted":
                self.arr[index] = Pair(key, value)
                self.size += 1
                if self.capacity // 2 <= self.size:
                    self.resize()
                return
            # index is full with same key, replace
            elif self.arr[index].key == key:
                self.arr[index].val = value
                return

            # open address, linear probe
            index += 1
            index = index % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.arr[index] != None:
            if (self.arr[index].val != "deleted" and 
            self.arr[index].key == key):
                return self.arr[index].val
            
            index += 1
            index = index % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False
        
        index = self.hash(key)

        while True:
            if self.arr[index].key == key:
                self.arr[index].val = "deleted"   # maintains probe order
                self.size -= 1
                return True
            index += 1
            index = index % self.capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = []

        for i in range(self.capacity):
            new_arr.append(None)
        
        old_arr = self.arr
        self.arr = new_arr
        self.size = 0

        for pair in old_arr:
            if pair:
                if pair.val != "deleted":
                    self.insert(pair.key, pair.val)

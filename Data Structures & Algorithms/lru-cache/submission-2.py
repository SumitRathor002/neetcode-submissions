class LRUCache:

    class Node:
        def __init__(self, key, val, prev = None, next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    # def printll(self):
    #     print(f"self.head {self.head.val if self.head else None}, self.tail {self.tail.val if self.tail else None}")
    #     print("printing ll")
    #     temp = self.tail 
    #     while temp is not None:
    #         print(f"[{temp.key}:{temp.val}] -> " , end = '')
    #         temp = temp.next
    #     print("ll ended")

    def reshuffle(self, key):
        # print("Reshuffling")
    
        node = self.cache[key]
        prev = node.prev
        next = node.next 

        if self.head is node:
            return
        
        # set the prev's next to node's next
        # set the next prev to node's prev
        if prev is not None:
            prev.next = next
            
        if next is not None:
            next.prev = prev

        self.head.next = node
        node.prev = self.head
        self.head = self.head.next
        node.next = None

        if self.tail is node:
            self.tail = next

        

    def get(self, key: int) -> int:
        # print(self.cache)
        # print(f"get {key}")
        if key in self.cache:
            self.reshuffle(key)
            # self.printll()
            return self.cache[key].val
        
        # self.printll()
        return -1


    def put(self, key: int, value: int) -> None:
        # print(self.cache)
        # print(f"put {key}")
        if key in self.cache:
            self.reshuffle(key)
            self.cache[key].val = value
        else:
            # if length exceeds remove lru key-node
            if len(self.cache) == self.capacity:
                self.cache.pop(self.tail.key)
                if self.tail.next:
                    self.tail.next.prev = None
                self.tail = self.tail.next

            # create a new node
            node = self.Node(key, value)
            self.cache[key] = node
            node.prev = self.head
            if self.head:
                self.head.next = node

            self.head = node

            if self.tail is None:
                self.tail = node

        # self.printll()



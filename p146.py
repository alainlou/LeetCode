from collections import defaultdict

class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.lookup = defaultdict(lambda: None)
        self.capacity = capacity
        self.size = 0

    def make_head(self, node: ListNode):
        # it's already the head
        if node is self.head or self.capacity == 1:
            return

        # update tail if necessary
        if node is self.tail:
            self.tail = self.tail.prev

        # update pointers
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        # put it at self.head
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return

    def get(self, key: int) -> int:
        # try to do a lookup
        ret = self.lookup[key]

        # make head
        if ret is not None:
            self.make_head(ret)
            return ret.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # special case for just updating the node
        if self.get(key) != -1:
            self.head.val = value
            return

        # special case when list is empty
        if self.size == 0:
            self.head = ListNode(key, value)
            self.tail = self.head
            self.lookup[key] = self.head
            self.size += 1
            return

        # special case for capacity == 1 and list is full
        if self.size == 1 and self.capacity == 1:
            del self.lookup[self.head.key]
            self.head.key = key
            self.head.val = value
            self.lookup[key] = self.head
            return

        # capacity >= 2
        # evict if necessary
        if self.size == self.capacity:
            # evict
            tmp = self.tail
            self.tail = self.tail.prev
            del self.lookup[tmp.key]
            del tmp
            self.size -= 1

        # update the head node
        new_head = ListNode(key, value)
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head
        self.lookup[key] = self.head
        self.size += 1

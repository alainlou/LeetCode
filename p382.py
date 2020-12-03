from random import randrange
from DS.ListNode import ListNode

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

        self.len = 0

        curr = head

        while curr:
            self.len += 1
            curr = curr.next


    def getRandom(self) -> int:
        idx = randrange(self.len)
        curr = self.head

        for _ in range(idx):
            curr = curr.next

        return curr.val

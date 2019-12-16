from DS.ListNode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        def swap(before, after):
            tmp = None
            if not after:
                return before
            tmp = after.next
            after.next = before
            before.next = tmp
            if before.next:
                before.next = swap(before.next, before.next.next)
            return after
        return swap(head, head.next)
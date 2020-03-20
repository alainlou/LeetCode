from DS.ListNode import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1

        k %= n

        slow, fast = head, head
        for _ in range(k):
            fast = fast.next

        if fast == head:
            return head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        tmp = slow.next
        slow.next = None
        fast.next = head
        head = tmp

        return head

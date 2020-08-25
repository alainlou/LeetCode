from DS.ListNode import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        odd_head = slow.next
        slow.next = None
        curr = odd_head.next
        odd_head.next = None

        while curr:
            tmp = curr.next
            curr.next = odd_head
            odd_head = curr
            curr = tmp

        curr = head
        while curr and odd_head:
            tmp = curr.next
            curr.next = odd_head
            odd_head = odd_head.next
            curr.next.next = tmp
            curr = tmp

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = slow.next
        slow.next = None

        head = self.sortList(head)
        tmp = self.sortList(tmp)

        ret = None

        if not tmp or (head and head.val < tmp.val):
            ret = head
            head = head.next
        else:
            ret = tmp
            tmp = tmp.next

        curr = ret

        while head and tmp:
            if head.val < tmp.val:
                curr.next = head
                head = head.next
                curr = curr.next
            else:
                curr.next = tmp
                tmp = tmp.next
                curr = curr.next

        while head:
            curr.next = head
            head = head.next
            curr = curr.next

        while tmp:
            curr.next = tmp
            tmp = tmp.next
            curr = curr.next

        return ret

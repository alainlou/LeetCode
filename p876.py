from DS.ListNode import ListNode

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

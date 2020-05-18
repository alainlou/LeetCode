# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        odd_head = head
        even_head = head.next

        odd_curr = odd_head
        even_curr = even_head

        while odd_curr and odd_curr.next and even_curr and even_curr.next:
            odd_curr.next = odd_curr.next.next
            even_curr.next = even_curr.next.next
            odd_curr = odd_curr.next
            even_curr = even_curr.next

        while odd_curr and odd_curr.next:
            odd_curr.next = odd_curr.next.next
            if odd_curr.next is None:
                break
            odd_curr = odd_curr.next

        while even_curr and even_curr.next:
            even_curr.next = even_curr.next.next
            even_curr = even_curr.next

        odd_curr.next = even_head

        return odd_head

from DS.ListNode import ListNode

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = list1
        for _ in range(a-1):
            first = first.next
        second = first
        for _ in range(b-a+2):
            second = second.next
        first.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = second
        return list1
        
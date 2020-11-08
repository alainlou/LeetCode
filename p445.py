from DS.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        curr = l1
        while curr:
            num1 *= 10
            num1 += curr.val
            curr = curr.next
        curr = l2
        while curr:
            num2 *= 10
            num2 += curr.val
            curr = curr.next
        num = num1 + num2
        if num < 10:
            return ListNode(num)
        ret = ListNode(num%10)
        while num != 0:
            ret.val = num%10
            ret = ListNode(0, ret)
            num //= 10
        return ret.next

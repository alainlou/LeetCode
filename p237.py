from DS.ListNode import ListNode

class Solution:
    def deleteNode(self, node: ListNode):
        tmp = node.next
        node.val = node.next.val
        node.next = node.next.next
        del tmp

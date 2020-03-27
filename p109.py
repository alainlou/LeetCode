from DS import ListNode, TreeNode

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def recurse(head):
            if head is None:
                return None
            if head.next is None:
                return TreeNode(head.val)
            slow, fast = head, head.next.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            ret = TreeNode(slow.next.val)
            tmp = slow.next.next
            slow.next = None
            ret.left = recurse(head)
            ret.right = recurse(tmp)

            return ret

        return recurse(head)

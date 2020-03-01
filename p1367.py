from functools import lru_cache

from DS import ListNode, TreeNode

class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        @lru_cache(None)
        def recurse(node, root):
            if node is None or root is None:
                return False
            if node.next is None and root.val == node.val:
                return True
            elif root.val == node.val:
                return recurse(node.next, root.left) or recurse(node.next, root.right) or recurse(head, root.left) or recurse(head, root.right)
            else:
                return recurse(head, root.left) or recurse(head, root.right)

        return recurse(head, root)

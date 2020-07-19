from DS.TreeNode import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        q1 = [p]
        q2 = [q]

        while len(q1) > 0 and len(q2) > 0:
            curr1 = q1.pop(0)
            curr2 = q2.pop(0)
            if curr1.val != curr2.val:
                return False
            if curr1.left:
                if curr2.left:
                    q1.append(curr1.left)
                    q2.append(curr2.left)
                else:
                    return False
            if curr2.left and not curr1.left:
                return False
            if curr1.right:
                if curr2.right:
                    q1.append(curr1.right)
                    q2.append(curr2.right)
                else:
                    return False
            if curr2.right and not curr1.right:
                return False

        return True

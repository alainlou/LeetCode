from DS.TreeNode import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []

        curr = root

        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        node = self.stack.pop()

        curr = node.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

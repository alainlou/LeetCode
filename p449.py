from ast import literal_eval
from DS.TreeNode import TreeNode

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        nodes = []
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            nodes.append(node.val if node is not None else None)
            if node is not None:
                q.append(node.left)
                q.append(node.right)
        return str(nodes)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = literal_eval(data)
        if data == [None]:
            return None
        data = list(data)
        root = TreeNode(data.pop(0))
        q = [root]
        while len(q) > 0 and len(data) > 0:
            curr = q.pop(0)
            if data[0] is not None:
                curr.left = TreeNode(data[0])
            data.pop(0)
            if data[0] is not None:
                curr.right = TreeNode(data[0])
            data.pop(0)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        return root

from DS.TreeNode import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            nodes.append(node.val if node is not None else None)
            if node is not None:
                q.append(node.left)
                q.append(node.right)
        return nodes

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
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
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        return root
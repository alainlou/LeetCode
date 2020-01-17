from DS.Node import Node

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = [(root, 0)]
        while len(q) > 0:
            curr = q.pop(0)
            curr_node = curr[0]
            curr_level = curr[1]
            curr_node.next = None if len(q) == 0 or q[0][1] > curr_level else q[0][0]
            if curr_node.left is not None:
                q.extend([(curr_node.left, curr_level+1), (curr_node.right, curr_level+1)])
        return root

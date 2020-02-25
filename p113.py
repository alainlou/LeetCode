from DS.TreeNode import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        solution = []

        def recurse(node, sum, path):
            if node is None:
                return
            path.append(node.val)
            sum -= node.val
            if node.left is None and node.right is None and sum == 0:
                solution.append(path[:])
            recurse(node.left, sum, path)
            recurse(node.right, sum, path)
            sum += node.val
            path.pop(-1)

        recurse(root, sum, [])

        return solution

from DS.TreeNode import TreeNode

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        left = []
        right = []
        def traverse(root, arr):
            if not root:
                return
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)
        traverse(root1, left)
        traverse(root2, right)
        left_point = 0
        right_point = 0
        ans = []
        while left_point < len(left) and right_point < len(right):
            if left[left_point] < right[right_point]:
                ans.append(left[left_point])
                left_point += 1
            else:
                ans.append(right[right_point])
                right_point += 1
        while left_point < len(left):
            ans.append(left[left_point])
            left_point += 1
        while right_point < len(right):
            ans.append(right[right_point])
            right_point += 1
        return ans

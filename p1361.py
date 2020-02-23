class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [None]*n
        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] is not None:
                    return False
                parent[leftChild[i]] = i
            if rightChild[i] != -1:
                if parent[rightChild[i]] is not None:
                    return False
                parent[rightChild[i]] = i

        if parent.count(None) != 1:
            return False

        return True

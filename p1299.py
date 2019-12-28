class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right = [float('-inf') for _ in range(n)]
        right[-1] = -1
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i+1])
        return right

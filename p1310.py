class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        left = [None]*n
        left[0] = 0
        right = [None]*n
        right[-1] = 0
        mask = 0
        for i in range(n):
            mask ^= arr[i]
        for i in range(1, n):
            left[i] = left[i-1]^arr[i-1]
        for i in range(2, n+1):
            right[-i] = right[-i+1]^arr[-i+1]
        ans = []
        for q in queries:
            ans.append(mask^left[q[0]]^right[q[1]])
        return ans

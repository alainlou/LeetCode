class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0
        window = 0
        ans = 0
        for i in range(k):
            window += arr[i]
        if window/k >= threshold:
            ans += 1
        for i in range(k, n):
            window += arr[i]
            window -= arr[i-k]
            if window/k >= threshold:
                ans += 1
        return ans

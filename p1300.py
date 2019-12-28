class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        replace = min(round(target/n), arr[0])
        best = abs(target-replace*n)
        ans = replace
        for i in range(1, n):
            target -= arr[i-1]
            replace = max(arr[i-1], min(round(target/(n-i)), arr[i]))
            curr = abs(target-replace*(n-i))
            if curr < best:
                best = curr
                ans = replace
        return ans

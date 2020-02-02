class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)//2
        ans = 0
        count = [0 for _ in range(max(arr)+1)]
        for num in arr:
            count[num] += 1
        count.sort()
        for i in range(len(count)-1, -1, -1):
            if count[i] == 0:
                continue
            if n <= 0:
                break
            n -= count[i]
            ans += 1
        return ans

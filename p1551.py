class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        mid = n
        for i in range(n//2):
            ans += mid-(2*i+1)

        return ans

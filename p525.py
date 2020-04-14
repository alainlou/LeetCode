class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        indices = {0: -1}
        ans = 0

        for i, n in enumerate(nums):
            if n == 0:
                balance -= 1
            else:
                balance += 1

            if balance in indices:
                ans = max(ans, i - indices[balance])
            else:
                indices[balance] = i

        return ans

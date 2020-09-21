class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0

        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)):
                if j+i < len(arr)+1:
                    ans += sum(arr[j:j+i])

        return ans

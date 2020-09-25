from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def mod(n1, n2):
            return 1 if int(n1+n2) > int(n2+n1) else -1

        nums.sort(key=cmp_to_key(mod), reverse=True)

        while len(nums) > 1 and nums[0] == '0':
            del nums[0]

        return ''.join(nums)

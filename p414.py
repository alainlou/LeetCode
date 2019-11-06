class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -99999999999999
        second = -99999999999999
        third = -99999999999999
        for num in nums:
            if num > first:
                first = num
        for num in nums:
            if num < first and num > second:
                second = num
        for num in nums:
            if num < second and num > third:
                third = num
        return third if third != -99999999999999 else first
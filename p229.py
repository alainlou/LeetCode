class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        count1, count2 = 0, 0
        l = len(nums)

        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                num1 = n
                count1 = 1
            elif count2 == 0:
                num2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        ans = []
        if nums.count(num1) > l/3:
            ans.append(num1)
        if nums.count(num2) > l/3:
            ans.append(num2)

        return ans

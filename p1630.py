class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)

        for i in range(n):
            cop = nums[l[i]:r[i]+1]
            cop.sort()
            new = True
            diff = cop[1]-cop[0]
            for j in range(2, len(cop)):
                if cop[j]-cop[j-1] != diff:
                    new = False
                    break
            ans.append(new)

        return ans

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = float('inf')
        two = float('inf')

        for n in nums:
            if n < one:
                one = n
            elif n > two:
                return True
            elif n > one:
                two = min(two, n)

        return False

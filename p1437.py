class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        countdown = 0
        for n in nums:
            if n == 1:
                if 0 < countdown:
                    return False
                else:
                    countdown = k
            else:
                countdown -= 1 if countdown > 0 else 0
        return True

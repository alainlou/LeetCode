class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        return num%4 == 0 and self.isPowerOfFour(num//4)

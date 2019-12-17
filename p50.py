class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n//2 == n/2:
            tmp = self.myPow(x, n//2)
            return tmp*tmp
        else:
            return self.myPow(x, n//2) * self.myPow(x, n-n//2)
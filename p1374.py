class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        elif n == 2:
            return "ab"
        elif n%2 == 1:
            if n//2%2 == 0:
                return "".join(list(self.generateTheString(n//2)) + ['c']*(n//2+1))
            else:
                return "".join(list(self.generateTheString(n//2+1)) + ['c']*(n//2))
        else:
            if n//2%2 == 0:
                return "".join(['a']*(n//2-1) + ['b']*(n//2+1))
            else:
                return "".join(['a']*(n//2) + ['b']*(n//2))

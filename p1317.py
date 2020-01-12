class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(n):
            for c in str(n):
                if c == '0':
                    return False
            return True
        for i in range(n):
            if check(i) and check(n-i):
                return [i, n-i]

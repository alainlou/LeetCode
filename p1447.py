class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []

        def no_common_divisor(x, y):
            for i in range(2, min(x, y)+1):
                if x%i == 0 and y%i == 0:
                    return False
            return True

        for i in range(2, n+1):
            for j in range(1, i):
                if no_common_divisor(i, j):
                    ans.append(str(j)+'/'+str(i))

        return ans

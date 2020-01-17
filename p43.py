class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        if m == 0 or n == 0:
            return ""
        ans = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                ans += (ord(num1[i])-48)*(ord(num2[j])-48)*pow(10, (m-1+n-1)-(i+j))
        return str(ans)

class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(s):
            ans = ''
            num = 0
            start = float('inf')
            end = float('-inf')
            n = len(s)
            i = 0
            while i < n:
                if ord('0') <= ord(s[i]) <= ord('9'):
                    num *= 10
                    num += int(s[i])
                elif s[i] == '[':
                    balance = 1
                    start = i+1
                    j = i+1
                    while balance != 0 and j < n:
                        if s[j] == ']':
                            balance -= 1
                        elif s[j] == '[':
                            balance += 1
                        j += 1
                    end = j-1
                    i = end
                    ans += num*dfs(s[start:end])
                    num = 0
                else:
                    ans += s[i]
                i += 1
            return ans

        return dfs(s)

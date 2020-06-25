from collections import defaultdict

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        table = defaultdict(int)
        ans = []

        def removeEnd(s):
            if len(s) < 3 or s[-1] != ')' or not s[-2].isnumeric():
                return s
            for i in range(len(s)-3, -1, -1):
                if not s[i].isnumeric():
                    if s[i] == '(':
                        return s[:i]
                    else:
                        return s
            return s

        for n in names:
            ref = n
            sub = removeEnd(n)

            if sub in table and sub + '(' + str(table[sub]) + ')'== ref:
                table[sub] += 1
                ref = sub
                sub = removeEnd(sub)

            if n in table:
                tmp = n + '(' + str(table[n]) + ')'
                while tmp in table:
                    table[n] += 1
                    tmp = n + '(' + str(table[n]) + ')'
                table[tmp] += 1
                table[n] += 1
                ans.append(tmp)
            else:
                table[n] += 1
                ans.append(n)

        return ans

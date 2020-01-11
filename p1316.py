class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        solved = set()
        strings = set()
        ans = 0
        for i in range(1, n//2+1):
            for j in range(0, n-i):
                if (j, i) in solved:
                    continue
                count = 1
                p = text[j:j+i]
                left = j+i
                right = j+2*i
                while right < n+1:
                    s = text[left:right]
                    if p != s:
                        break
                    count += 1
                    left += i
                    right += i
                    if count%2 == 0 and text[j:j+i*count] not in strings:
                        solved.add((j, i*count))
                        strings.add(text[j:j+i*count])
                        ans += 1
        return ans

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(result)
        if n < max(map(len, words)):
            return False
        words.append(result)
        m = len(words)
        c2n = {}
        n2c = {}
        def recurse(word_idx, char_idx, carry):
            if char_idx >= n:
                if carry == 0:
                    print(c2n)
                return carry == 0
            if word_idx == m:
                return recurse(0, char_idx+1, carry//10) if carry%10 == 0 else False
            if char_idx > len(words[word_idx])-1:
                return recurse(word_idx+1, char_idx, carry)
            c = words[word_idx][~char_idx]
            sign = -1 if word_idx == m-1 else 1
            if c in c2n:
                return recurse(word_idx+1, char_idx, carry+sign*c2n[c])
            for i in range(10):
                if i not in n2c and (c != words[word_idx][0] or i != 0):
                    c2n[c] = i
                    n2c[i] = c
                    if recurse(word_idx+1, char_idx, carry+sign*i):
                        return True
                    del c2n[c]
                    del n2c[i]
        return recurse(0, 0, 0)

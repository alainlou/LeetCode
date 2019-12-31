class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        def check(lhs, rhs, dictionary):
            left = 0
            right = 0
            for i in lhs:
                left += dictionary[i] * lhs[i]
            for i in rhs:
                right += dictionary[i] * rhs[i]
            return left == right

        def process(curr, basket, lhs, rhs, chars, leading):
            if len(curr) == len(chars):
                if check(lhs, rhs, curr):
                    return True
                return False
            for i in range(len(basket)):
                char = chars[len(curr)]
                if char in leading and basket[i] == 0:
                    continue
                tmp = basket.pop(i)
                curr[char] = tmp
                if process(curr, basket, lhs, rhs, chars, leading):
                    return True
                del curr[char]
                basket.insert(i, tmp)
            return False

        basket = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        chars = []
        leading = set()
        lhs = {}
        rhs = {}
        for w in words:
            n = len(w)
            leading.add(w[0])
            for i in range(n):
                if w[i] not in chars:
                    chars.append(w[i])
                if w[i] not in lhs:
                    lhs[w[i]] = pow(10, n-i-1)
                else:
                    lhs[w[i]] += pow(10, n-i-1)
        n = len(result)
        leading.add(result[0])
        for i, c in enumerate(result):
            if c not in chars:
                chars.append(c)
            if c not in rhs:
                rhs[c] = pow(10, n-i-1)
            else:
                rhs[c] += pow(10, n-i-1)

        return process({}, basket, lhs, rhs, chars, leading)
                
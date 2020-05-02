class Solution:
    def maxDiff(self, num: int) -> int:

        def operate(num, x, y):
            ret = str(num).replace(str(x), str(y))
            return int(ret) if (len(ret) > 0 and ret[0] != '0') else 0

        least = float('inf')
        most = float('-inf')

        for i in range(10):
            for j in range(10):
                res = operate(num, i, j)
                least = min(least, res if res != 0 else least)
                most = max(most, res if res != 0 else most)

        return most - least

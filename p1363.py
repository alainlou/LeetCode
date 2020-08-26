class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:

        dig_sum = sum(digits)
        count = [0] * 10
        for d in digits:
            count[d] += 1
        case = dig_sum % 3

        def process(count, to_remove, n):
            i = 0
            counter = 0

            while counter < n and i < 3:
                if count[to_remove[i]] > 0:
                    count[to_remove[i]] -= 1
                    counter += 1
                else:
                    i += 1

            if counter < n:
                return False

            return True

        if case == 1:
            copy = count[:]
            if process(count, [1, 4, 7], 1):
                pass
            elif process(copy, [2, 5, 8], 2):
                count = copy
        elif case == 2:
            copy = count[:]
            if process(count, [2, 5, 8], 1):
                pass
            elif process(copy, [1, 4, 7], 2):
                count = copy

        ans = []
        for i in range(9, -1, -1):
            if i == 0 and len(ans) == 0 and count[0] > 0:
                ans.extend("0")
            else:
                ans.extend([str(i)]*count[i])
        return "".join(ans)

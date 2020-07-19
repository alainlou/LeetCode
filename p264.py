class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        cand = [0, 0, 0]

        for _ in range(n-1):
            while ans[cand[0]]*2 <= ans[-1]:
                cand[0] += 1
            choose = (0, ans[cand[0]]*2)
            while ans[cand[1]]*3 <= ans[-1]:
                cand[1] += 1
            if ans[cand[1]]*3 < choose[1]:
                choose = (1, ans[cand[1]]*3)
            while ans[cand[2]]*5 <= ans[-1]:
                cand[2] += 1
            if ans[cand[2]]*5 < choose[1]:
                choose = (2, ans[cand[2]]*5)
            cand[choose[0]] += 1
            ans.append(choose[1])

        return ans[-1]

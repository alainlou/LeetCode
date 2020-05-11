class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        table = {i: 0 for i in range(1, N+1)}
        flip_table = {i: 0 for i in range(1, N+1)}

        for pair in trust:
            table[pair[1]] += 1
            flip_table[pair[0]] += 1

        for k, v in table.items():
            if v == N-1 and flip_table[k] == 0:
                return k

        return -1

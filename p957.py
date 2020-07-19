class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        prev, curr = cells, [0]+cells[1:-1]+[0]
        memo = {}
        arr = []
        cycle_len = None

        for i in range(N):
            s = ''.join(map(str, prev))
            if s in memo:
                cycle_len = i-memo[s]
                break
            memo[s] = i
            arr.append(s)
            for j in range(1, len(curr)-1):
                curr[j] = 1 if prev[j-1] == prev[j+1] else 0
            prev = curr[:]

        return arr[(N-(len(arr)-cycle_len))%cycle_len+(len(arr)-cycle_len)] if cycle_len else prev

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        curr_color = colors[0]
        times = [neededTime[0]]
        idx = 1
        ans = 0

        while idx < n:
            if curr_color != colors[idx]:
                if len(times) > 1:
                    ans += sum(times) - max(times)
                curr_color = colors[idx]
                times = []

            times.append(neededTime[idx])
            idx += 1

        if len(times) > 1:
            ans += sum(times) - max(times)

        return ans

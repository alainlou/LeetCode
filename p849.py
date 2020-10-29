class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = float('-inf')
        ans = 1

        for i, s in enumerate(seats):
            if s:
                if last == float('-inf'):
                    ans = max(ans, i)
                else:
                    ans = max(ans, (i-last)//2)
                last = i

        ans = max(ans, len(seats)-1-last)

        return ans

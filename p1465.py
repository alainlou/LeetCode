class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()

        a = float('-inf')
        b = float('-inf')

        for i in range(1, len(verticalCuts)):
            a = max(a, verticalCuts[i] - verticalCuts[i-1])

        for i in range(1, len(horizontalCuts)):
            b = max(b, horizontalCuts[i] - horizontalCuts[i-1])

        return (a * b) % (10**9 + 7)

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        for n in sorted(count.keys()):
            if count[n] != 0:
                tmp = count[n]
                for j in range(n, n+k):
                    if j not in count:
                        return False
                    count[j] -= tmp
                    if count[j] < 0:
                        return False
        return True
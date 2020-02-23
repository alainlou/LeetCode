import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        def find_divisors(num):
            ans = []
            for i in range(1, int(math.sqrt(num))+1):
                if num%i == 0:
                    ans.extend([i, num//i])
            return sorted(ans)

        ans1 = find_divisors(num+1)
        n1 = len(ans1)
        ans2 = find_divisors(num+2)
        n2 = len(ans2)

        return [ans1[n1//2-1], ans1[n1//2]] \
            if abs(ans1[n1//2-1] - ans1[n1//2]) < abs(ans2[n2//2-1] - ans2[n2//2]) \
            else [ans2[n2//2-1], ans2[n2//2]]

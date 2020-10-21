class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for a in asteroids:
            if len(ans) == 0:
                ans.append(a)
            else:
                if a < 0:
                    while len(ans) > 0 and ans[-1] > 0 and -a > ans[-1]:
                        del ans[-1]
                    if len(ans) > 0 and ans[-1] > 0 and -a == ans[-1]:
                        del ans[-1]
                    elif len(ans) == 0 or -a > ans[-1]:
                        ans.append(a)
                else:
                    ans.append(a)

        return ans

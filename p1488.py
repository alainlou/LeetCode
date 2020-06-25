class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1]*len(rains)
        seen = {}
        places = []

        for i, r in enumerate(rains):
            if r == 0:
                ans[i] = 1
                places.append(i)
            else:
                if r in seen and len(places) > 0:
                    flag = False
                    for j, p in enumerate(places):
                        if p > seen[r]:
                            ans[places.pop(j)] = r
                            flag = True
                            break
                    if not flag:
                        return []
                elif r in seen:
                    return []
                seen[r] = i

        return ans

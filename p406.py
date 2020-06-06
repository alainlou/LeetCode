class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[0])
        ans = [None]*len(people)

        while len(people) > 0:
            curr = people.pop(0)
            count = 0
            for i, a in enumerate(ans):
                if a is not None and a[0] < curr[0]:
                    count += 1
                elif i - count == curr[1]:
                    ans[i] = curr
                    break

        return ans

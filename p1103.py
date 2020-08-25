class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        end, rem = 0, 0

        for i in range(141242):
            if i*(i+1)//2 > candies:
                rem = candies - (i*(i-1)//2)
                break
            end = i

        ans = [0]*num_people

        for i in range(1, end+1):
            ans[(i-1)%num_people] += i

        ans[(end)%num_people] += rem

        return ans

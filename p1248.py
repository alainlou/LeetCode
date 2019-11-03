class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odds = [-1]
        for i in range(n):
            if nums[i]%2 == 1:
                odds.append(i)
        if len(odds) < k+1:
            return 0
        odds.append(len(nums))
        answer = 0
        for i in range(1, len(odds)-k):
            left = i
            right = left + k-1
            answer += (odds[left]-odds[left-1]) * (odds[right+1]-odds[right])
        return answer
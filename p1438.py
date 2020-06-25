class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0
        right = 1
        window = [nums[0]]
        window_max = [nums[0]]
        window_min = [nums[0]]
        ans = 0

        while left < n+1 and right < n+1:
            if window_max[0] - window_min[0] <= limit:
                ans = max(ans, right-left)
                if right == n:
                    break
                # extend the window
                window.append(nums[right])
                while len(window_max) > 0 and window_max[-1] < nums[right]:
                    del window_max[-1]
                while len(window_min) > 0 and window_min[-1] > nums[right]:
                    del window_min[-1]
                # always append (avoid len < 1)
                window_max.append(nums[right])
                window_min.append(nums[right])
                right += 1
            else:
                tmp = window.pop(0)
                if tmp == window_max[0]:
                    window_max.pop(0)
                if tmp == window_min[0]:
                    window_min.pop(0)
                left += 1

        return ans

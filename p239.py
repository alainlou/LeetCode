class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = [nums[0]]
        window_monotonic = [nums[0]]
        ans = [nums[0]]

        for i in range(1, n):
            # append to ans
            ans.append(window_monotonic[0])

            # update sliding window and maxqueue
            window.append(nums[i])
            while len(window_monotonic) > 0 and window_monotonic[-1] < nums[i]:
                del window_monotonic[-1]
            # always append (avoid len < 1)
            window_monotonic.append(nums[i])

            # pop from front of sliding window and maxqueue if necessary
            if len(window) > k:
                tmp = window.pop(0)
                if tmp == window_monotonic[0]:
                    window_monotonic.pop(0)

        ans.append(window_monotonic[0])

        return ans[k:]

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = [nums[0]]
        window_monotonic = [nums[0]]
        ans = nums[0]

        for i in range(1, n):
            # curr represents the best including nums[i]
            curr = nums[i] + max(0, window_monotonic[0])
            ans = max(ans, curr)

            # update sliding window and maxqueue
            window.append(curr)
            while len(window_monotonic) > 0 and window_monotonic[-1] < curr:
                del window_monotonic[-1]
            # always append (avoid len < 1)
            window_monotonic.append(curr)

            # pop from front of sliding window and maxqueue if necessary
            if len(window) > k:
                tmp = window.pop(0)
                if tmp == window_monotonic[0]:
                    window_monotonic.pop(0)

        return ans

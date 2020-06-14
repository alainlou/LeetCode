class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left_dp = [float('inf')]*len(arr)

        left = 0
        right = 0
        curr = arr[right]

        while right < len(arr):
            if curr == target:
                left_dp[right] = min(left_dp[right], right-left+1)
            if left == right or curr < target:
                right += 1
                if right == len(arr):
                    break
                curr += arr[right]
                left_dp[right] = left_dp[right - 1]
            else:
                curr -= arr[left]
                left += 1

        right_dp = [float('inf')]*len(arr)
        left = len(arr)-1
        right = len(arr)-1
        curr = arr[left]

        while left > -1:
            if curr == target:
                right_dp[left] = min(right_dp[left], right-left+1)
            if left == right or curr < target:
                left -= 1
                if left == -1:
                    break
                curr += arr[left]
                right_dp[left] = right_dp[left + 1]
            else:
                curr -= arr[right]
                right -= 1

        ans = float('inf')
        for i in range(len(arr)-1):
            ans = min(ans, left_dp[i] + right_dp[i+1])

        return ans if ans != float('inf') else -1

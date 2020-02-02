class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = [0]*n

        def recurse(idx):
            if memo[idx] > 0:
                return memo[idx]
            curr = 1
            for i in range(idx-1, idx-d-1, -1):
                if i < 0 or arr[i] >= arr[idx]:
                    break
                curr = max(curr, 1+recurse(i))
            for i in range(idx+1, idx+d+1):
                if i >= n or arr[i] >= arr[idx]:
                    break
                curr = max(curr, 1+recurse(i))
            memo[idx] = curr
            return curr

        for i in range(len(arr)):
            recurse(i)

        return max(memo)

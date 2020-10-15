class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def gcd(a, b):
            if a%b == 0:
                return b
            return gcd(b, a%b)

        n = len(nums)
        k %= n
        if k == 0:
            return
        cycles = gcd(n, k)
        for idx in range(cycles):
            prev = nums[idx-k]
            for _ in range(n//cycles):
                tmp = nums[idx]
                nums[idx] = prev
                prev = tmp
                idx = (idx+k)%n

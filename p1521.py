class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        # Initialize ans and number of bits (2^20 = 1048576)
        ans = abs(-10e9 - target)
        NUM_BITS = 20

        # masking_level for every bit in our [left, right) window
        masking_level = [0]*NUM_BITS

        # We start off with a bitmask of just the first number
        for i in range(NUM_BITS):
            masking_level[i] = 1 if ((1 << i) & arr[0]) else 0

        # Update the masking level (we only care about the zeros)
        # sign represents whether you are taking away from (by adding a new number)
        # or adding to the mask (by taking away an old number)
        def update(num, masking_level, sign):
            for i in range(NUM_BITS):
                masking_level[i] += sign * (-1 if (not (1 << i) & num) else 0)

        # Get the actual number from the masking level array
        def get_num(masking_level):
            ans = 0
            for i in range(NUM_BITS):
                ans += (1 << i) if (masking_level[i] > 0) else 0
            return ans

        left, right = 0, 1

        while left < len(arr) and right < len(arr):
            curr = get_num(masking_level)
            ans = min(ans, abs(curr - target))
            if left == right-1 or curr > target:
                # increment the right pointer if we want to decrease the curr value
                update(arr[right], masking_level, 1)
                right += 1
            else:
                # otherwise increment the left pointer
                update(arr[left], masking_level, -1)
                left += 1

        return ans

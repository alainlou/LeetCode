class Solution:
    def isPossible(self, target: List[int]) -> bool:

        def recurse(target, prev_sum):
            if prev_sum == len(target):
                return True
            curr_sum = 0
            max_value = float('-inf')
            max_idx = None
            for i in range(len(target)):
                if target[i] > max_value:
                    max_value = target[i]
                    max_idx = i
                curr_sum += target[i]
            curr_sum -= max_value
            tmp = target[max_idx]
            target[max_idx] -= curr_sum
            if target[max_idx] < 1:
                return False
            return recurse(target, tmp)

        return recurse(target, sum(target))

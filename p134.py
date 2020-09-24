class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        left, right = 0, 0

        curr = 0

        while True:
            flag = False
            while curr+gas[right%n]-cost[right%n] >= 0:
                curr += gas[right%n]-cost[right%n]
                right += 1
                if right-left > n:
                    flag = True
                    break
            while curr+gas[right%n]-cost[right%n] < 0:
                left -= 1
                curr += gas[left]-cost[left]
                if right-left >= n:
                    flag = True
                    break
            if flag:
                break

        return left%n if curr >= 0 else -1

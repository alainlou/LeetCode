class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_count = [0]*k

        for n in arr:
            mod_count[n%k] += 1

        if mod_count[0]%2 != 0:
            return False

        for i in range(1, len(mod_count)-1):
            if mod_count[i] != mod_count[k-i]:
                return False

        return True

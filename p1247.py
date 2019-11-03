class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        if(len(s1) != len(s2)):
            return -1
        xy_mismatch = 0
        yx_mismatch = 0
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                xy_mismatch += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx_mismatch += 1
        if (xy_mismatch + yx_mismatch)%2 == 1:
            return -1
        answer = xy_mismatch//2 + yx_mismatch//2
        xy_mismatch %= 2
        yx_mismatch %= 2
        if xy_mismatch and yx_mismatch:
            answer += 2
        return answer
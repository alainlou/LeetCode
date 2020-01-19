class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: x[0])
        idx = 1
        while idx < len(clips):
            if clips[idx][1] < clips[idx-1][1]:
                del clips[idx]
            else:
                idx += 1
        ans = 0
        end = 0
        for i in range(T+1):
            if i > end:
                best = end
                idx = 0
                while idx < len(clips):
                    if clips[idx][0] > end:
                        break
                    if clips[idx][1] < best:
                        del clips[idx]
                        continue
                    best = max(best, clips[idx][1])
                    idx += 1
                end = best
                ans += 1
        return ans if end >= T else -1

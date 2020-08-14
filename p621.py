class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0]*26

        for t in tasks:
            counts[ord(t)-ord('A')] += 1

        counts.sort()

        empty = (counts[-1]-1) * n

        for i in range(24, -1, -1):
            empty -= min(counts[-1]-1, counts[i])

        return len(tasks) if empty < 0 else len(tasks) + empty

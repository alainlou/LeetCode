class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.memo = {}

    def find(self, range_start, range_end, search_start=0, search_end=None):
        if search_end == None:
            search_end = len(self.arr)

        if range_start >= search_end or range_end <= search_start:
            return float('inf')
        if (range_start, range_end) in self.memo:
            return self.memo[(range_start, range_end)]
        if range_start == range_end-1:
            return self.arr[range_start]

        mid = (search_start+search_end)//2
        left = self.find(range_start, min(range_end, mid), search_start, mid)
        right = self.find(max(range_start, mid), range_end, mid, search_end)
        ans = left if left <= right else right

        if search_start == range_start and search_end == range_end:
            self.memo[(range_start, range_end)] = ans

        return ans

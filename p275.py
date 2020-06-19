class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = len(citations)
        mid = (lo+hi)//2

        while lo != mid:
            if citations[mid] >= len(citations)-mid:
                hi = mid
            else:
                lo = mid+1
            mid = (lo+hi)//2

        if mid > len(citations) - 1:
            return 0

        ret = len(citations)-mid
        return ret if citations[mid] >= len(citations)-mid else ret-1

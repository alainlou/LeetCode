class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*1001
        for t in trips:
            arr[t[1]] += t[0]
            arr[t[2]] -= t[0]

        tmp = 0
        for e in arr:
            tmp += e
            if tmp > capacity:
                return False

        return True

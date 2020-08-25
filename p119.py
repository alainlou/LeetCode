class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []
        curr = [1]

        for i in range(rowIndex):
            prev = curr[:]
            for j in range(1, i+1):
                curr[j] = prev[j-1]+prev[j]
            curr.append(1)

        return curr

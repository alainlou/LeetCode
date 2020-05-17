class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        idx = 0

        for i in range(1, n+1):
            if idx >= len(target):
                break
            if i < target[idx]:
                operations.append('Push')
                operations.append('Pop')
            elif i == target[idx]:
                operations.append('Push')
                idx += 1
            else:
                break

        return operations

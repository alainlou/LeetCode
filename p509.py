class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def check(arr):
            dx, dy = arr[1][0]-arr[0][0], arr[1][1]-arr[0][1]

            if dx == 0 and dy == 0:
                return False

            for i in range(2, 4):
                if arr[i][1] != arr[i-1][1]-dx or arr[i][0] != arr[i-1][0]+dy:
                    return False
                dx, dy = arr[i][0]-arr[i-1][0], arr[i][1]-arr[i-1][1]

            return True

        points = [p1, p2, p3, p4]
        arr = []

        def dfs(idx):
            if idx == 4:
                return check(arr)
            ans = False

            for i in range(len(points)):
                tmp = points.pop(i)
                arr.append(tmp)
                ans = max(ans, dfs(idx+1))
                arr.pop()
                points.insert(i, tmp)

            return ans

        return dfs(0)

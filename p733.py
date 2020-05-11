class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_colour = image[sr][sc]
        if old_colour == newColor:
            return image
        m, n = len(image), len(image[0])
        q = [(sr, sc)]

        while len(q) > 0:
            curr = q.pop(0)
            image[curr[0]][curr[1]] = newColor
            adjacent = [(curr[0]-1, curr[1]), (curr[0]+1, curr[1]), (curr[0], curr[1]-1), (curr[0], curr[1]+1)]
            for point in adjacent:
                if 0 <= point[0] < m and 0 <= point[1] < n and image[point[0]][point[1]] == old_colour:
                    q.append(point)

        return image

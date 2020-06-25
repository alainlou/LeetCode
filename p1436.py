class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        visited = set()

        for p in paths:
            cities.add(p[0])
            cities.add(p[1])
            visited.add(p[0])

        cities -= visited
        return list(cities)[0]

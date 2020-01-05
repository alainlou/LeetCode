class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set()
        q = [(id, 0)]
        distance = {}
        while len(q) > 0:
            curr = q.pop(0)
            if curr[0] in visited:
                continue
            visited.add(curr[0])
            distance[curr[0]] = curr[1]
            for f in friends[curr[0]]:
                if f not in visited:
                    q.append((f, curr[1]+1))
        counts = {}
        for node in distance:
            if distance[node] == level:
                for vid in watchedVideos[node]:
                    if vid not in counts:
                        counts[vid] = 1
                    else:
                        counts[vid] += 1
        return [node[0] for node in sorted(counts.items(), key=lambda item: (item[1], item[0]))]

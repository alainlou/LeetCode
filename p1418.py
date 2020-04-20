from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        data = defaultdict(lambda: defaultdict(int))
        tables = set()
        foods = set()

        for order in orders:
            data[order[1]][order[2]] += 1
            tables.add(int(order[1]))
            foods.add(order[2])

        tables = sorted(tables)
        foods = sorted(foods)

        ans = [["Table"]]
        for f in foods:
            ans[0].append(f)

        for t in tables:
            ans.append([str(t)])
            for f in foods:
                ans[-1].append(str(data[str(t)][f]))

        return ans

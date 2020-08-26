class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = []
        deck.sort(reverse=True)
        for d in deck:
            if len(res) > 0:
                res.insert(0, res.pop())
            res.insert(0, d)

        return res

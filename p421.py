from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_num(self, n):
        curr = self.root
        for i in range(31, -1, -1):
            if (1<<i)&n:
                curr = curr.children[i]
        curr.end = True

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        t = Trie()

        for n in nums:
            t.add_num(n)

        for n in nums:
            mask = n
            curr = t.root
            while len(curr.children.keys()) > 0:
                flag = False
                for i in range(31, -1, -1):
                    if not (1<<i)&n and i in curr.children:
                        mask ^= (1<<i)
                        curr = curr.children[i]
                        flag = True
                        break
                if not flag:
                    k = min(curr.children.keys())
                    mask ^= (1<<k)
                    curr = curr.children[k]
            ans = max(ans, mask)

        return ans

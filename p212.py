class TrieNode:
    def __init__(self):
        self.val = None
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for c in s:
            index = ord(c)-ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.val = s


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()

        for w in words:
            t.insert(w)

        ans = set()
        node = t.root

        def dfs(i, j, node):
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j] == '.':
                return
            node = node.children[ord(board[i][j])-ord('a')]
            if node and node.val:
                ans.add(node.val)
            tmp = board[i][j]
            board[i][j] = '.'
            if node:
                dfs(i+1, j, node)
                dfs(i-1, j, node)
                dfs(i, j+1, node)
                dfs(i, j-1, node)
            board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, node)

        return list(ans)

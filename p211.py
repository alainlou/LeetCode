from DS.Trie import TrieNode

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c)-ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.end = True

    def search(self, word: str) -> bool:

        def dfs(node, chr_idx):
            if not node:
                return False
            if chr_idx == len(word):
                return node.end
            if word[chr_idx] == '.':
                for c in node.children:
                    if c:
                        tmp = dfs(c, chr_idx+1)
                        if tmp:
                            return True
                return False
            else:
                idx = ord(word[chr_idx])-ord('a')
                return dfs(node.children[idx], chr_idx+1)

        return dfs(self.root, 0)

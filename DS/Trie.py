class TrieNode:
    def __init__(self):
        self.end = False
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
        node.end = True

    def find(self, s):
        node = self.root
        for c in s:
            index = ord(c)-ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.end

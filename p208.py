class TrieNode:

    def __init__(self, val, end):
        self.val = val
        self.is_end = end
        self.children = [None]*26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode('', False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.head
        for i, c in enumerate(word):
            if curr.children[ord(c)-ord('a')] is None:
                curr.children[ord(c)-ord('a')] = TrieNode(c, False)
            if i == len(word) - 1:
                curr.children[ord(c)-ord('a')].is_end = True
            curr = curr.children[ord(c)-ord('a')]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.head
        for i,c in enumerate(word):
            if curr.children[ord(c)-ord('a')] is None:
                return False
            curr = curr.children[ord(c)-ord('a')]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.head
        for i,c in enumerate(prefix):
            if curr.children[ord(c)-ord('a')] is None:
                return False
            curr = curr.children[ord(c)-ord('a')]
        return True


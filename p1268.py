class TrieNode:
    def __init__(self):
        self.end = False
        self.count = 0
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, str):
        node = self.root
        for c in str:
            index = ord(c)-ord('a')
            if(node.children[index] == None):
                node.children[index] = TrieNode()
            node = node.children[index]
        node.end = True
        node.count += 1
        
    def find(self, s):
        answer = []
        node = self.root
        for c in s:
            index = ord(c)-ord('a')
            if(node.children[index] == None):
                return []
            node = node.children[index]
        self.recurse(node, answer, s)
        return answer
        
    def recurse(self, node, answer, word):
        if node == None or len(answer) > 2:
            return
        if node.end:
            count = node.count
            while count > 0 and len(answer) < 3:
                answer.append(word)
                count -= 1
        for i in range(26): 
            if node.children[i] != None:
                self.recurse(node.children[i], answer, word+chr(i+ord('a')))
                         
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer = []
        t = Trie()
        for p in products:
            t.insert(p)
        for i in range(1, len(searchWord)+1):
            q = searchWord[:i]
            answer.append(t.find(q))
        return answer
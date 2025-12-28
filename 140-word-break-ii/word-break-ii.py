from collections import defaultdict

class Trie():
    def __init__(self):
        self.children = dict()
        self.isEnd = False
    
    def insert(self, val: str):
        root = self
        for char in val:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
        root.isEnd = True

    def search(self, string: str) -> bool:
        root = self
        for word in string:
            if word in root.children:
                root = root.children[word]
            else:
                return False
        return root.isEnd

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        def dfs(word:str):
            if not word:
                return [[]]
            
            results = []
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if trie.search(prefix):
                    rest = dfs(word[i:])
                    for combi in rest:
                        results.append([prefix] + combi)
            return results
        retVal = dfs(s)
        return [' '.join(k) for k in retVal]
        
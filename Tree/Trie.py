# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class Trie:
    def __init__(self):
        self.isEnd=False
        self.charset=collections.defaultdict(Trie)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Trie()
        self.root.isEnd=True
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr=self.root
        for ch in word:
            curr=curr.charset[ch]
        curr.isEnd=True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node,w):
            
            for i in range(len(w)):
                if w[i]=='.':
                    for ch in node.charset.keys():
                        if dfs(node.charset[ch],w[i+1:]):
                            return True
                    else:
                        return False
                elif node.charset.get((w[i])):
                    node=node.charset[w[i]]
                else:
                    return False
            return node.isEnd
        return dfs(self.root,word)

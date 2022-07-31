class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char_mapping = {}
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for char in word:
            if char not in node.char_mapping:
                node.char_mapping[char] = Trie()
            node = node.char_mapping[char]
        node.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for char in word:
            if char not in node.char_mapping:
                return False
            node = node.char_mapping[char]
        return node.isEnd == True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for char in prefix:
            if char not in node.char_mapping:
                return False
            node = node.char_mapping[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

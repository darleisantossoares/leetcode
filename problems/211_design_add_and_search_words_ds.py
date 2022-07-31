class WordDictionary:
    def __init__(self):
        self.d = defaultdict(set)


    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)


    def search(self, word: str) -> bool:
        m = len(word)
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False

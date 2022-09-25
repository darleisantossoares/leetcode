class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True 

    def search(self, word):
        curr = self.root 
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word 

    def startsWith(self, prefix):
        curr = self.root 

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True 

if __name__ == '__main__':
    arvore = Trie()
    arvore.insert('Darlei')
    arvore.insert('Roberta')
    arvore.insert('Heloisa')
    arvore.insert('Peter')
    arvore.insert('Maria')
    arvore.insert('Gilmar')
    arvore.insert('Lumi')
    arvore.insert('Akemi')
    arvore.insert('Sakamoto')
    print(arvore.search('Darlei'))
    print(arvore.startsWith('Ak'))
    print(arvore.search('darlei'))




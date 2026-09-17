class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()

            node = node.children[character]

        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        node = self.root

        for character in word:
            if character not in node.children:
                return False

            node = node.children[character]

        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for character in prefix:
            if character not in node.children:
                return False

            node = node.children[character]

        return True
            
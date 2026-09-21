from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()

            node = node.children[character]

        node.word = word


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:

        rows = len(board)
        columns = len(board[0])

        trie = WordDictionary()

        for word in words:
            trie.addWord(word)

        root = trie.root
        result = []

        def dfs(row: int, column: int, parent: TrieNode) -> None:
            # Check board boundaries first
            if (
                row < 0
                or column < 0
                or row >= rows
                or column >= columns
            ):
                return

            character = board[row][column]

            # Visited cell or invalid Trie path
            if (
                character == "#"
                or character not in parent.children
            ):
                return

            # Move to the matching Trie node
            node = parent.children[character]

            # Collect a complete word
            if node.word is not None:
                result.append(node.word)

                # Prevent duplicate results
                node.word = None

            # Mark the board cell as visited
            board[row][column] = "#"

            dfs(row + 1, column, node)
            dfs(row - 1, column, node)
            dfs(row, column + 1, node)
            dfs(row, column - 1, node)

            # Backtrack: restore the cell
            board[row][column] = character

            # Optional Trie pruning
            if not node.children and node.word is None:
                del parent.children[character]

        for row in range(rows):
            for column in range(columns):
                dfs(row, column, root)

        return result
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i, x in enumerate(board): 
            for j, y in enumerate(x):
                if y == ".": 
                    continue

                if(y in rows[i] or y in cols[j] or y in squares[(i//3, j//3)]):
                    return False

                rows[i].add(y)
                cols[j].add(y)
                squares[(i//3, j//3)].add(y)
        
        return True

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                square_key = (r//3, c//3)

                if (val in rows[r] or val in cols[c] or val in squares[square_key]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)

        return True
                


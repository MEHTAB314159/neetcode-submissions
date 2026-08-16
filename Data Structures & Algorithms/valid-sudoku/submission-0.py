import collections
class Solution:
    def isValidSudoku(self,board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                if num in rows[r] or num in cols[c] or num in boxs[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    boxs[(r//3,c//3)].add(num)
        return True
                
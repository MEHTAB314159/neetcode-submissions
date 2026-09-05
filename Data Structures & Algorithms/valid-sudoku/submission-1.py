class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # nums = board[r][c]
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[r // 3,c // 3]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True



# This code checks whether a 9×9 Sudoku is valid. First, we create three defaultdict(set) dictionaries: rows stores the numbers already seen in each row, cols stores numbers seen in each column, and squares stores numbers seen in each 3×3 box. Then for r in range(9) goes through each row, and for c in range(9) goes through each column. r and c are just variable names we chose for row and column. For every cell, board[r][c] gives the current value. If the value is ".", we use continue to skip it because it is empty. If it is a number, we check whether that number is already in rows[r], cols[c], or squares[(r//3, c//3)]. If it is already present in any one of them, we return False because there is a duplicate. If it is not present, we add the number to its row, column, and 3×3 square using .add(). The program repeats this for all 81 cells, and if no duplicate is found, it returns True.

# 🧠 Easy memory trick

# Every number → Check Row + Column + Box → Duplicate? False → Otherwise Add → Continue → Finished? True.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # PSEUDOCODE:
        # Create hash maps to track digits seen in each row, column, and 3x3 sub-box.
        # Each key maps to a set of digits already encountered.
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (row_group, col_group)

        # PSEUDOCODE:
        # Loop through every cell in the 9x9 Sudoku board.
        for r in range(9):
            for c in range(9):

                # PSEUDOCODE:
                # If the cell is empty, it does not affect Sudoku validity.
                # Skip it and move to the next cell.
                if board[r][c] == ".":
                    continue

                # PSEUDOCODE:
                # Check if the current digit has already appeared
                # - in the same row
                # - in the same column
                # - in the same 3x3 sub-box
                # If so, the board is invalid.
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                # PSEUDOCODE:
                # Mark the digit as seen in the current row.
                rows[r].add(board[r][c])

                # PSEUDOCODE:
                # Mark the digit as seen in the current column.
                columns[c].add(board[r][c])

                # PSEUDOCODE:
                # Determine the 3x3 sub-box using integer division,
                # then mark the digit as seen in that box.
                squares[(r // 3, c // 3)].add(board[r][c])

        # PSEUDOCODE:
        # If no duplicates were found after checking all cells,
        # the Sudoku board satisfies all validity rules.
        return True

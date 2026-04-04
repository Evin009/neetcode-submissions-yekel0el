class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # arr length not 9
        if len(board) != 9:
            return False

        # checking each row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # checking each col
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # checking each 3x3 matrix sq
        for square in range(9): # dvides sudoku to 9 squres of 3x3
            seen = set() # every interation of sqaure seen start empty
            # checking row and col inside individual 3x3 blocks
            for i in range(3):
               for j in range(3):
                row = (square//3) * 3 + i
                col = (square % 3) * 3 + j
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        return True 
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking - base case when is complete 
        # choose, explore and undo
        # find all posible choices

        ''' 
        base case - len(cur word) == word(len) match if its same and return true or return 

        every square we have 4 choices up, down, left or right
        explore one with recursion till the base case
        then undo 

        '''
        ROWS = len(board)
        COLS = len(board[0])
        vis = set()

        # recursion for travelling along a starting point
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # if row or col less than zero or greater than rows and cols
            # if word
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in vis):
                return False
            
            # chose a path
            vis.add((r, c))

            # explore 4 different path 
            res = (dfs(r + 1, c, i + 1) or
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or
                  dfs(r, c - 1, i + 1) )
            #undo choice 
            vis.remove((r, c))
                
            return res
            

        # now run the recursion for all the start points in board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False





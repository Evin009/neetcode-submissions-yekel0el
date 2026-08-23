class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
# first we need all possible patterns with n pairs of parenthesis - backtracking
# chose - explore - undo
# when is complete when all the open and close brackets are used or == n
# two choices either add open or close 
# first always open as long as open is avaiable 
# chose - explore more using recursion after all done return - undo
# 

        res = []
        stack = []

        def backtrack(openN, closeN):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            
            
            # add open
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res

            # add close
            

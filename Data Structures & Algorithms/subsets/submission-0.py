class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtraking
        # when is complete
        # what choices do I have - 
        #herr: include a number or dont include a number

        # run the backtrack till the index of arr
        # once the indx out of range base case reached
        # record the base case stored in sol to res
        # backtrack to prev case
        # move to next choice

        res = [] # final result
        sol = [] # base case sol
        n = len(nums)
        def backtrack(i):
            ''' when is complete''' 
            if i == n:
                res.append(sol[:]) #append base case in sol to res
                return 
            

            ''' what choices do i have? '''
            # dont include num and move to next idx
            backtrack(i + 1)

            # include num and move to next idx/ level
            sol.append(nums[i])
            backtrack(i + 1)

            # backtrack after reaching the base case
            sol.pop()


        backtrack(0)
        return res
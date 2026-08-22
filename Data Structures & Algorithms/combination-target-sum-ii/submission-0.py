class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # all possible list of numbers that adds to target
        # only once can be used 
        
        # either include the element or not include the element
        candidates.sort()
        res = []
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            
            if total > target or i >= len(candidates) :
                return
            
            # include the current element
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            # not inlcude cur elemnt
            # skip nums that are same 
            while  i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        return res



            # '''
            #[1,2,2,4,6,5,9]
            # [9]
            # [2]
            # [2, 2]
            # [2, 2, 4] = 8 @
            # [2, 2, 6] 
            # [2, 2, 1]
            # [2, 2, 1, 5]
            # [2, 4]
            # [2, 4, 6]
            # [2, 4, 1]
            
            # '''
        

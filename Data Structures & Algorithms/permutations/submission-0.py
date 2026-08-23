class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutation - order matters

        res = []

        n = len(nums)

        hashmap = {}

        for i in nums:
            hashmap[i] = False

        def backtrack(cur):
            if len(cur) == n:
                res.append(cur[:])
                return
            
            for i in nums:
                if hashmap[i] == False:
                    cur.append(i)
                    hashmap[i] = True
                    backtrack(cur)
                    cur.pop()
                    hashmap[i] = False
        
        backtrack([])
        return res
            


        '''
        []
        i = 1 -> [1]
                 [1,2]
                 [1,2,3] 
                 [1,2]
        i = 2 -> []
        '''

            


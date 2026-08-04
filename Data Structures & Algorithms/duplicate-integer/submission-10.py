class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if val appear more than once return True
        # add elements onto the hasmap 
        # if a val in hasmap return false

        hashmap = {}

        for idx, val in enumerate(nums):
            if val in hashmap:
                return True

            hashmap[val] = idx
        
        return False
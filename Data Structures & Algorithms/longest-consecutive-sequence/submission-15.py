class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return len of longest consecutive seq
        # excatly 1 greater than before 
        # edge cases - negetive values?, can have seq starting differently 
        # 

        # use hash to keep track of elements 
        # only add element to hash if difference between last added element is one greater than current

        if len(nums) == 0:
            return 0
        res = 0
        hashset = set(nums)

        for num in hashset:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                res = max(res, length)
        return res
                
        
        


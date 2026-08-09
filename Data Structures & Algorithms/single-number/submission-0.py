class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor 
        # 1 xor 0 = 0; 1 xor 1 = 0

        res = 0
        for num in nums:
            # all the duplicates will be zero and only the single value will be returned
            res ^= num
        
        return res
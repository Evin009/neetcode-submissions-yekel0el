class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        performing forward and backward product on a single arr
        '''

        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i] #updating prefix with product of val of nums
        # res = [1,1,2,6]

        suffix = 1
        for i in range(n-1, -1,-1):
            # mulitpyin the val directily onto res array
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

        # nums = [1,2,3,4]

        # res = [24,12,8,6]
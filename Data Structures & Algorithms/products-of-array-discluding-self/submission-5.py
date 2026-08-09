class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given - int arr nums
        # output[i] - product of all the elements of nums except nums[i]
        # return - output (Arr)

        '''
        - zeros? Y
        - duplicates? Y
        - negetives ? Y
        '''

        # pattern: product of elements before nums[i] and after nums[i] needed so prefix product pattern can be used

        n = len(nums)
        res = [1] * n

        prefix = [1] * n
        suffix = [1] * n

        # product of every val to the left of the idx: [1,1,2,6]
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # product of every value to the right of i [24,12,4,1]
        suffix[n-1] = 1
        for i in range(n-2, -1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res
        

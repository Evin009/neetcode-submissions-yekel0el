class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
        
            m = (r + l) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                # check right cause all small values in right now
                l = m + 1
            else:   
                # check left cause all small values in left now
                r = m - 1
        
        return res
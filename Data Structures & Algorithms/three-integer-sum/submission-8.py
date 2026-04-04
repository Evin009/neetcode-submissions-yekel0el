class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #[-1, -1, 0, 1]
        res = []

        for i in range(len(nums)):
            if nums[i] > 0: # all negetive should be one left side if not break
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue # if two numbers same skip the other
            
            l, r  = i + 1, len(nums) - 1
            
            while l < r:
                sum = nums[i] + nums[r] + nums[l]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    val = [nums[i], nums[r], nums[l]]
                    if val not in res:
                        res.append(val)
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return res
                



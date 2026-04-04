class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hashmap = {}

        # for idx, val in enumerate(nums):
        #     hashmap[val] = idx
        
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         s = 0 - (nums[i] + nums[j])
        #         if s in hashmap.keys() and i != hashmap[s] and j != hashmap[s]:
        #             val = [nums[i], nums[j], s]
        #             val.sort()
        #             if val not in res:
        #                 res.append(val)
        # return res

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            l , r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                elif total == 0:
                    val = [nums[i], nums[l], nums[r]]
                    if val not in res:
                        res.append(val)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    
                        
        return res


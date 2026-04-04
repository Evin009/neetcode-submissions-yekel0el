class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}

        for idx, val in enumerate(nums):
            hashmap[val] = idx
        
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = 0 - (nums[i] + nums[j])
                if s in hashmap.keys() and i != hashmap[s] and j != hashmap[s]:
                    val = [nums[i], nums[j], s]
                    val.sort()
                    if val not in res:
                        res.append(val)
        return res
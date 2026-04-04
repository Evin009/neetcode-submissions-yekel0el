class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        
        for i in range(len(nums)):
                hashmap[nums[i]] = i        
        for idx, val in enumerate(nums):
                diff = target - val
                if diff in hashmap and hashmap[diff] != idx:
                        return [idx, hashmap[diff]]
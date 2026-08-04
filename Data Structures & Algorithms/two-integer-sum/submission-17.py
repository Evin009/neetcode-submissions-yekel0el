class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices i and j such that both the sums add to target
        # use a hashmap to strore the idex and value pair
        # take difference of cur val and target if the diff exist in hasmap return their idx

        hashmap = {}

        for i in range(len(nums)):
                hashmap[nums[i]] = i
        
        diff = 0
        for idx, val in enumerate(nums):
                diff = target - val
                if diff in hashmap and hashmap[diff] != idx:
                        return [idx, hashmap[diff]]
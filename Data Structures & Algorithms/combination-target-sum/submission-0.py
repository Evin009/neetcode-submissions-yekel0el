class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # two choices at every index
        #- keep the current number and stay at the index
        # - move to next number and index

        # add sol to res if sum == target
        res = []

        def backtrack(i, currentList, total):
            # when is complete
            if total == target:
                res.append(currentList[:])
                return
            if total > target or i >= len(nums):
                return
            
            # add the same element
            currentList.append(nums[i])
            backtrack(i, currentList, total + nums[i])
            currentList.pop()

            # not add the same element and chose next in idex
            backtrack(i + 1, currentList, total)
            

           
        backtrack(0, [], 0)
        return res

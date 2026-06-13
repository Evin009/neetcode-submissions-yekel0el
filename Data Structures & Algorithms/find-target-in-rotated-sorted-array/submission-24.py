class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #both halves are sorted 
        # [5,1,2,3,4] t = 1
        # 

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[left]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

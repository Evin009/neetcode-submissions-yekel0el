class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated sorted arr - gets divided in two sorted halves
        # we need the min value
        l = 0
        r = len(nums) - 1

        min_val = nums[0]
        while l <= r:
            # if arr not rotated return the left most value
            if nums[r] > nums[l]:
                min_val = min(min_val, nums[l])
                break

            mid = (l + r) // 2
            min_val = min(min_val, nums[mid])


            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return min_val

        

        #edge cases - neg val, zeros, not rotated
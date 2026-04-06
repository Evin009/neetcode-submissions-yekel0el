class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search - O(log n)
        # rotated - in middle there is a division where left and right halves are sorted independetly
        # return idx of the target else -1

        # EDGE CASES:
        # either left or right ptr is the target
        # the array is empty
        # the element range is huge 

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            if n == 0:
                return -1
            
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            
            #[4,5,6,7,0,1,2]; t = 0 , [4,5,6], t= 5

            if nums[m] > nums[l]:
                if nums[l] < target < nums[m]:
                    r = m - 1 
                else:
                    l = m + 1
            else:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
            

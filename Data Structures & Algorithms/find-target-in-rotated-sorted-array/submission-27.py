class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # searching, target= binary search using index
        # sorted array rotated - divided in two parts left and right

        # find the target in a sorted array

        '''
        EDGE CASES
        - empty array return -1 
        - cant find = -1
        - not rotated = check if arr is rotated or not?
        - neg valeus> - yes
        - duplicates? - no all val unique
        '''
        # t = 1
        # [3,4,5,6,1,2] mid = 6 =? target - return mid else 
        # L      m   R

        l, r = 0 ,len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # divide in two parts 
            elif nums[mid] > nums[l]:
                # left part
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # right park
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1    
            
                
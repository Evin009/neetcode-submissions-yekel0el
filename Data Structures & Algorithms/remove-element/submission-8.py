class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # tmp = []
        # for i in nums:
        #     if i != val:
        #     tmp.append(i)
        
        # # making it in-place
        # for j in range(len(tmp)):
        #     nums[j] = tmp[j]
        
        # return len(tmp)

        # 2 pointers

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

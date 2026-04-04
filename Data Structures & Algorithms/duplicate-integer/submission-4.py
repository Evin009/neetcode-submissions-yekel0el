class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
    
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        for key, cnt in count.items():
            if cnt > 1:
                return True
        return False

        # count = set()

        # for i in nums:
        #     if i in count:
        #         return True
        #     count.add(i)
        # return False



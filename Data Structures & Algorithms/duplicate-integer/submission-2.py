class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i,0)

        res = []
        for val, cnt in count.items():
            res.append([val,cnt])
        res.sort()

        for items in res:
            if items[1] > 1:
                return True
        return False

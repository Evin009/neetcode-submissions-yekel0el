class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force - check element by element if its cur + 1 in hashset count + 1
        # for each value we keep on checking if it has a sequence and stops when its all counted

        res = 0
        store = set(nums)

        for num in nums:
            if num - 1 not in store:
                streak, curr = 0, num   
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res
            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        hashset = set(nums) # (2,3,4,5,10,20)
        longest = 0

        for num in nums:
            if num - 1 not in hashset:
                start = num
                seq_count = 1
                while start + 1 in hashset:
                    seq_count += 1
                    start += 1
                longest = max(longest, seq_count)
            
        return longest

                    
                    
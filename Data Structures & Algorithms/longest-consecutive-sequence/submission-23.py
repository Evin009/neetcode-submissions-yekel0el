class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given - arr of ints
        # what to do - lenght of the longest consecuttive seq which can be formed
        # return - int (length)

        '''
        Contraints: zeros - Y, duplitcates = Y, negetives = N
        '''
        '''
        - elements not in consective order in array
        - we use hashset cause consecutive vales
        - we check if num + 1 in hashset also ,making sure if num - 1 is not to be sure its start of a sequence 
        - increment the counter each time num + 1is their in the end compare to longest one seen so far and returning the max
        '''
        
        longest = 0
        hash_nums = set(nums)

        if len(nums) == 0:
            return 0
        
        for num in nums:
            if num - 1 not in hash_nums:
                count = 1
                cur = num

                while cur + 1 in hash_nums:
                    count += 1
                    cur += 1
            
                longest = max(count, longest)
        
        return longest
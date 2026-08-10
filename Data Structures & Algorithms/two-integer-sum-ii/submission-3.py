class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given - arr of int, sorted in ascending order
        # return - list of two indices idx. 1 < idx 2
        # ehat to do  - look for two numbers so that they add upto the trargte and return their indices

        # O(1) - no hashmaps, nned to use two pointers

        l, r = 0, len(numbers) - 1

        
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            if total < target:
                l += 1
            else:
                r -= 1
        

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # increment the last idex value 
        # if last index val is 9 move to idx before and check if its 9 if yes continue looping backward else append 1 and change the idx val to 0

        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        digits.insert(0,1)
        return digits
        

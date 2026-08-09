class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Tc - O(1)

        '''
        concept - instead of linear calculation we will use divide and conquer method
        - if each step square the base and divide the power
        - if n is even return the res if n is odd mutilpy the base to the res
        '''

        if n == 0:
            return 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        res = 1
        power = abs(n)

        while power > 0:
            # if power is odd
            if power % 2 == 1:
                res *= x
            
            x *= x
            power //= 2
        
        return res if n >= 0 else 1/res
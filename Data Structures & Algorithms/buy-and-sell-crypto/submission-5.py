class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        - two pointers 
        - the num in front has to be greater else move on
        '''

        l, r = 0, 0
        max_profit = 0

        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
            else:
                l += 1
        
        return max_profit
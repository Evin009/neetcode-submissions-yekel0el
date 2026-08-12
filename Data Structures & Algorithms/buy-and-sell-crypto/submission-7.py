class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given - array of ints
        # price[i] - price on the ith day
        # return max profit possible?

        # profit when - the prices are higher in later day
        # variable sliding window
        '''
        - two pointer approch is to have a fast and slow pointer
        - update right only if l < r
        - else make l = r (if l > r) we are not counting them
        '''

        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            
            else:
                l = r
            
            r += 1
        
        return maxP
            

            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # to have a profit - we need a min possible val on left
        # that's why if we see any val less than the current val immediately update the ptr to it

        l = 0
        maxP = 0
        for r in range(1, len(prices)):
            # if price l < price r then only profit can happen
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]  
                maxP = max(profit, maxP)
            
            else:
                l = r

        return maxP
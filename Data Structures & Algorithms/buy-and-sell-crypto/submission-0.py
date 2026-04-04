class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]

                max_diff = max(diff, max_diff)
        return max_diff

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0

        max_profit = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            
        return max_profit


            


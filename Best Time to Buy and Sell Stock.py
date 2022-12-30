class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            ans = prices[i] - min_price
            max_profit = max(max_profit, ans)

        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            if prices[r] - prices[l] > max:
                max = prices[r] - prices[l]
        return max
                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0
        while(right < (len(prices))):
            if prices[left] > prices[right]:
                left += 1
            else:
                currentprofit = prices[right] - prices[left]
                if currentprofit > maxprofit:
                    maxprofit = currentprofit
                right += 1  
        return maxprofit
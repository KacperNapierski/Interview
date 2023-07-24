class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1 #left = buy, right = sell
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if max_profit < profit:
                    max_profit = profit



            else:
                left = right
            
            right += 1
            
        return max_profit

#2657 ms, faster than 39.30% 
#25 MB, less than 39.35%
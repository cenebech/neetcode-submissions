class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set up everything I need
        left = 0
        right = 1
        max_profit = 0

        #while loop
        while right < len(prices):
            
            #is today's price cheaper for buying
            if prices[right] < prices[left]:
                left = right
                
            #calculate profit and choose the best
            else:
                profit = prices[right] - prices[left]
                max_profit = max(profit,max_profit)
                
            #move counter forward
            right += 1

        return max_profit

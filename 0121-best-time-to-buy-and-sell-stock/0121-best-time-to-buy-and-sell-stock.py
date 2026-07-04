class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        profit=0
        for i in range(1,len(prices)):
            if(buyprice>prices[i]):
                # must buy
                buyprice=prices[i]
            else:
                profit=max(profit,prices[i]-buyprice)
        return profit
            
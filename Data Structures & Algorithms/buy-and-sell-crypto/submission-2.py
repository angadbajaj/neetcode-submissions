class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r = 0,1
        
        while r < len(prices):
            maxP = max(maxP, prices[r]-prices[l])
            if prices[l] < prices[r]:
                r+=1
            else:
                l = r
                r += 1
        return maxP

        
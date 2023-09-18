from typing import List

'''
Logic:
take two pointers buy and sell, start from start 0 and 1
buy = left sell = right
max profit = prices[right] - prices[left]
set left = right when u find lowest buying price

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy
        right = 1 #sell
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right+=1


        return max_profit

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))

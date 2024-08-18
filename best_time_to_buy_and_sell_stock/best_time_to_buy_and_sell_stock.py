from typing import List
from test_data import prices
import time
start_time = time.time()


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


# prices =[7,11,1,2,4]
print(Solution().maxProfit(prices))
print("--- %s seconds ---" % (time.time() - start_time))

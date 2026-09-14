class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit = 0

        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                l=r
            r+=1
        return maxProfit



# For this question:

# prices = [10, 1, 5, 6, 7, 1]

# the goal is to buy on one day and sell on a later day so that we get the maximum profit. The code starts with l = 0 and r = 1, where l represents the buying day and r represents the selling day. So at first, l points to 10 and r points to 1. We check prices[l] < prices[r], which asks whether the selling price is greater than the buying price. Here 10 < 1 is false, so buying at 10 and selling at 1 would give a loss. Therefore, we do l = r, which means we move the buying pointer to the cheaper price 1. Then r += 1 moves the selling pointer to the next day. Now l points to 1 and r points to 5, so we can buy at 1 and sell at 5, giving a profit of 5 - 1 = 4. We store this in maxP, so maxP = 4. Then r moves to the next price, 6. We are still buying at 1, so the profit is 6 - 1 = 5, and maxP becomes 5. Next, r moves to 7, giving 7 - 1 = 6, so maxP becomes 6. Finally, r moves to the last price 1. Since the selling price 1 is not greater than the buying price 1, we don't calculate a profit; instead, we set l = r. Then r moves beyond the last index, so r < len(prices) becomes false and the loop stops. The final maxP is 6, meaning the best decision is to buy at price 1 and sell later at price 7, giving a profit of 6.

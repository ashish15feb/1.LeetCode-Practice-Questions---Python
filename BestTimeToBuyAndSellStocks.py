"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as
you like (ie, buy one and sell one share of the stock multiple times). However, you may
not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        haveShare = False
        profit = 0
        for i in range(len(prices)):
            if (haveShare == False):
                if (i + 1 < len(prices) and (prices[i] < prices[i + 1])):
                    haveShare = True
                    buyPrice = prices[i]
                    continue
                else:
                    continue
            else:  # sell
                if (i + 1 < len(prices) and (prices[i] > prices[i + 1])) or (i + 1 == len(prices)):
                    haveShare = False
                    sellPrice = prices[i]
                    profit = profit + sellPrice - buyPrice
                    continue
                else:
                    continue
        return (profit)

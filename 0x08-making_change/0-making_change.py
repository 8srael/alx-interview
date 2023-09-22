#!/usr/bin/python3

""" Task 0. Change comes from within"""


def makeChange(coins, total):
    """
        determines the fewest number of coins needed
        to meet a given amount total.
    """

    if total == 0:
        return 0
 
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[total] if dp[total] != float('inf') else -1

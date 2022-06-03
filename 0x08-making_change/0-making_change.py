#!/usr/bin/python3


def makeChange(coins, total):
    """make change algorithim"""
    dp = [total + 1] * (total +1)
    dp[0] = 0

    for a in  range(1, total + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    
    return dp[total]  if dp[total] != total + 1 else -1
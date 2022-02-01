"""
https://leetcode.com/problems/daily-temperatures/solution/

Given an array of coins that represent the daily money a child receives from the parent to put in the piggy bank,
return an array result such that result[ i ] is the number of days child has to wait after the nth day to get more
money. If no such day exists then keep result[ i ] = -1.

"""


def coin_wait(coins):
    n = len(coins)
    res = [-1] * n
    stack = []

    for curr_day, curr_coin in enumerate(coins):
        while stack and coins[stack[-1]] < curr_coin:
            prev_day = stack.pop()
            res[prev_day] = curr_day - prev_day
        stack.append(curr_day)

    return res


print(coin_wait([5, 10, 55, 45, 35, 65, 75, 15, 20, 30, 25]))
print(coin_wait([5, 10, 15, 20]))

## Coin change

Leetcode.: https://leetcode.com/problems/coin-change/

Algo

```
                | 0                             :if amount == 0
                |
coins(amount) = |
                |
                | 1 + min coins(amount-coin)    :else

```


### Implementation Top Down

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def _coins(amount, possible_coins,memo={}):

            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0
            min_coins = float('inf')
            for coin in possible_coins:
                if (amount-coin)>=0:
                    min_coins = min(min_coins, 1+_coins(amount-coin, possible_coins,memo))
            memo[amount] = min_coins
            return min_coins

        min_coins = _coins(amount, coins)
        return -1 if min_coins == float('inf') else min_coins
```

### Implementation with tabulation

```
def coins(amount, possible_coins):
   dp = [float('inf')]*(amount+1)
   dp[0] = 0
   for i in range(1, amount+1):
       for coin in possible_coins:
           if (i-coin) >= 0:
               dp[i] = min(dp[i], 1+dp[i-coin])
    return -1 if dp[amount] == float('inf') else dp[amount]
```



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def _coins(amount, possible_coins):
            dp = [float('inf')]*(amount+1)
            dp[0] = 0
            for i in range(1, amount+1):
                for coin in possible_coins:
                    if (i-coin) >= 0:
                        dp[i] = min(dp[i], 1+dp[i-coin])
            return -1 if dp[amount] == float('inf') else dp[amount]

        return _coins(amount, coins)

class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(n,memo={}):

            if n < 4:
                return n
            elif n in memo:
                return memo[n]
            else:
                memo[n]= climb(n-2,memo)+climb(n-1,memo)
                return memo[n]
        return climb(n)

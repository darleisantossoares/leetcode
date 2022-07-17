## House Robber

Leetcode.: https://leetcode.com/problems/house-robber/

Problema clássico de dp

### Top Down approaches

```
def rob(arr, i=0):
    if i >= len(arr):
        return 0
    else:
        return max(arr[i]+rob(arr, i+2), rob(arr, i+1))
```


_Memoization_

```
def rob(arr, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    if i >= len(arr):
        return 0
    else:
        lookup[i] = max(arr[i]+rob(arr, i+2, lookup), rob(arr, i+1, lookup))
        return lookup[i]
```

### Bottom Up

```
def rob(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i]+dp[i-2])
    return dp[n-1]
```

_With Space Optimization_

```
def rob(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    before_prev_dp = arr[0]
    prev_dp = max(arr[0], arr[1])
    for i in range(2, n):
        dp = max(prev_dp, arr[i]+before_prev_dp)
        before_prev_dp = prev_dp
        prev_dp = dp
    return prev_dp
```




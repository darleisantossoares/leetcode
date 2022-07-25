## Longest Increasing Subsequence

Leetcode.: https://leetcode.com/problems/longest-increasing-subsequence/

### Formula
```
                   |0                                                    :if i = |arr|
                   |
subsequence(i,prev)|subsequence(i+1,prev)                                :if arr[i] <= prev
                   |
                   |max(1+subsequence(i+1,arr[i]), subsequence(i+1,prev)) :otherwise
```

#### Top Down Approach
```
def subsequence(arr,i=0,prev=float('-inf'),cache={}):
    if i in cache:
        return cache[i]
    if i >= len(arr):
        return 0
    elif arr[i] <= prev:
        cache[i+1] = subsequence(arr,i+1,prev,cache)
        return cache[i+1]
    else:
        cache[i]= max(1+subsequence(arr,i+1,arr[i],cache), subsequence(arr,i+1,prev,cache))
        return cache[i]
```

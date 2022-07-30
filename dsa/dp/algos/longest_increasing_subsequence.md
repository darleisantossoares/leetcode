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
def subsequence(arr):
    def rec(arr, i, cache):
        if i in cache:
            return cache[i]
        maxlen=0
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                maxlen = max(maxlen, rec(arr,j,cache))
        cache[i]=1+maxlen
        return cache[i]
    cache={}
    return max([rec(arr,i,cache) for i in range(len(arr))])
```

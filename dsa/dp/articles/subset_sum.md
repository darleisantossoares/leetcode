## Subset Sum

The basic idea is to take or not, same decision as house robber and so on.

_Statement_

Given an array of strictly positive integer _arr_ and strictly positive integer _k_, count the number
of subsets that sums up to k.

_Example_

input:

arr=[1,2,3,1,4]

k = 6

output: 4

explanation: we have 4 subsets that sum up to 6:

[1,2,3],[1,1,4],[2,3,1] and [2,4]

### Formula

```
             |1                     :if k = 0
             |
subsets(k,i) |0                     :if i =|arr| or k <0
             |
             |subsets(k-arr[i],i+1) :otherwise
             |+ subsets(k,i+1)
```

### Implementations
#### Top Down
```
def subsets(arr,k,i,cache):
    if (k,i) in cache:
        return cache[(k,i)]
    elif k == 0:
        return 1
    elif i == len(arr) or k < 0:
        return 0
    else:
        cache[(k,i)]= subsets(k-arr[i],i+1) + subsets(k,i+1)
        return cache[(k,i)]
```



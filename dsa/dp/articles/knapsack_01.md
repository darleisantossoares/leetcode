## Dynamic Programming 0/1 Knapsack

*Statement*.:

When have _n_ items, each one of them has a value _Vi_ and a weight _Wi_, and we want to determine which items to take without exceeding the maximum weight _k_ while having a total value that is as big as possible, you are asked to return their total value.

### Formula

```
             |0                :if i == |v|
             |
knapsack(k,i)|knapsack(k,i+1)  :if Wi > k
             |
             |max(Vi + knapsack(k-Wi,i+1), knapsack(k,i+1)) :else
```

### The implementation of the algorithm
#### Top Down
```
def knapsack(values, weights, k, i=0, loopkup={}):
    if (k, i) in loopkup:
        return lookup[(k,i)]
    elif i == len(values):
        return 0
    elif weights[i] > k:
        lookup[(k,i)]= knapsack(values, weights, k, i+1, lookup)
        return lookup[(k,i)]
    else:
        lookup[(k,i)] = max(values[i]+knapsack(values, weights,k-weights[i],i+1,lookup), knapsack(values, weights,k,i+1,lookup))
        return lookup[(k,i)]
```



```
Supposed we are given an array and there are two elememnts
within a window of size k that are equal
```

def closeDuplicates(nums, k):
    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l + 1 > k:
            window.remove(nums[l])
            l + 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False



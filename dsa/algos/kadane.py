```
In this example for kadane we are going to find the subarray
with the largest sum.
```
def kadane(nums):
    maxsum = nums[0]
    cursum = 0

    for n in nums:
        cursum = max(cursum, 0)
        cursum += n
        maxsum = max(maxsum, cursum)
    return maxsum



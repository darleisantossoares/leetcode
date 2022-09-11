'''
In this example for kadane we are going to find the subarray
with the largest sum.
'''
def kadane(nums):
    maxsum = nums[0]
    cursum = 0

    for n in nums:
        cursum = max(cursum, 0)
        cursum += n
        maxsum = max(maxsum, cursum)
    return maxsum

# sliding window kadane
'''
return the left and right index of the max subarray sum,
assuming there is exatcly on result (no ties)
sliding window varion of kadane's O(n)
'''
def sliding_window_kadane(nums):
    maxsum = nums[0]
    curr = 0
    maxl, maxr = 0, 0
    l = 0
    for r in range(len(nums)):
        if curr < 0:
            cursum = 0
            l = r
        cursum += nums[r]
        if curr > maxsum:
            maxsum = curr
            maxl, maxr = l, r
    return [maxl, maxr]

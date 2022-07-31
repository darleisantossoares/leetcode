class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def rec(arr,i,cache):
            if i in cache:
                return cache[i]
            maxlen=0
            for j in range(i+1,len(arr)):
                if arr[j] > arr[i]:
                    maxlen=max(maxlen,rec(arr,j,cache))
            cache[i]=1+maxlen
            return cache[i]
        cache={}
        return max([rec(nums,i,cache) for i in range(len(nums))])

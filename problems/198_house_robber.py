class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(i, cache):

            if i >= len(nums): #Base Case
                return 0
            elif i in cache: # Memoization
                return cache[i]
            else:
                answer = max(nums[i] + helper(i + 2, cache), helper(i + 1, cache)) # algo
                cache[i] = answer
                return answer

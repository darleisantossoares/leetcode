class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        current, max_sum = nums[0], nums[0]

        for i in range(1, n):
            current = max(nums[i], current + nums[i])
            max_sum = max(max_sum, current)

        return max_sum

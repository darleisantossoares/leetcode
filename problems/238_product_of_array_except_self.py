class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, answer = [0]*n,[0]*n,[0]*n
        left[0]=1
        for i in range(1, n):
            left[i] = nums[i-1]*left[i-1]
        right[n-1] = 1
        for i in reversed(range(n-1)):
            right[i] = nums[i+1]*right[i+1]
        for i in range(n):
            answer[i] = left[i] * right[i]
        return answer

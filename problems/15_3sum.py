class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = list()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums,i,output)
        return output

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        low, high = i + 1, len(nums) - 1
        while low < high:
            total = nums[i] + nums[low] + nums[high]
            if total < 0:
                low += 1
            elif total > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1

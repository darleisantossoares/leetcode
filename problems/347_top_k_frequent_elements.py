class Solution:
    def topKFrequent(self, nums: List[int]: k: int) -> List[int]:
        if k == len(nums):
            return nums
        counter = collections.Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)

## Solution 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        items = sorted(count.items(), key=lambda item: -item[1])
        return [x for x, v in items[:k]]

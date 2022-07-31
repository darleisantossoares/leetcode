class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = []
        intervals.sort()
        cur = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if cur[1] > intervals[i][0]:
                count += 1
                cur = intervals[i] if intervals[i][1] < cur[1] else cur
            else:
                cur = intervals[i]
        return count

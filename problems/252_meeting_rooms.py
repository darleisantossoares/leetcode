class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()

        i = 1

        while i < len(intervals):

            if intervals[i][0] < intervals[i-1][1]:
                return False

            i += 1

        return True

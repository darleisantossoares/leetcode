class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in seen:
                sums = seen[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            seen[value] = i
        return maxlength

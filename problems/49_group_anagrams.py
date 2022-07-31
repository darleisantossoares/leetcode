class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countup(s: str):
            count = [0] * 26
            for c in s:
                count[ord(c) - orc('a')] += 1
            return tuple(count)
        groups = collections.defaultdict(list)
        for s in strs:
            count = countup(s)
            groups[count].append(s)
        return groups.values()

## Solution 2

class Solution2:
    def groupAnagrams(self, strs: List[int]) -> List[List[int]]:
        group = collections.defaultdict(list)
        for s in strs:
            group[tuple(sorted(s))].append(s) # another option is to coerce into string instead of tuple
        return group.values()

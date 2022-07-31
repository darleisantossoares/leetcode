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

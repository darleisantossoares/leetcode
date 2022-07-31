class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = {}
        l = 0
        max_count = 0
        for r, ch in enumerate(s):
            counter[ch] = counter.get(ch, 0) + 1
            max_count = max(max_count, counter[ch])

            if r+1 - l > max_count + k:
                counter[s[l]] -= 1
                l += 1
        return r+1 - l


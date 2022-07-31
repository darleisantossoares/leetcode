class Solution:
    def countSubstrings(self, s: str) -> int:

        N = len(s)
        total = 0

        #odd lenght of palindromes
        for left in range(N):
            right = left

            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1

        #even length palindromes
        for left in range(N - 1):
            right = left + 1

            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1


        return total

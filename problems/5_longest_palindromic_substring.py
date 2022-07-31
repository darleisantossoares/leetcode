class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        def expand_center(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1 : j]


        result = ''

        for i in range(n):
            ## odd length palindromes centered at i
            temp_palin = expand_center(i, i)

            result = temp_palin if len(temp_palin) > len(result) else result

            if i + 1 < len(s):
                ## even length palindromes centered around i, i+1
                temp_palin = expand_center(i, i + 1)

                if len(temp_palin) > len(result):
                    result = temp_palin


        return result

## Shortes Common Supersequence

Leetcode.: https://leetcode.com/problems/shortest-common-supersequence/

O algoritmo é o abaixo.

```
scs(s1,s2) = |s1|+|s2| - |lcs(s1,s2)|
```

lcs = longest common subsequence

LCS algo

```
         | 0                         | if i == |s1| or j == |s2| # Base Case
         |
LCS(i,j) | 1 + lcs(i+1,j+1)          | if s1[i]==s2[j]
         |
         | max(lcs(i+1,j),lcs(i,j+1) | else
```


Implementação usando tabulation

```
class Solution:
    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        res, i, j = "", 0, 0
        for c in self.longestCommonSubsequence(A, B):
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res+=c; i+=1; j+=1
        return res + A[i:] + B[j:]

    def longestCommonSubsequence(self, A: str, B: str) -> str:
        n, m = len(A), len(B)
        dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + A[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        return dp[-1][-1]
```

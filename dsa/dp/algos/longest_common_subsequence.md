## Longest Common Subsequence

Leetcode.: https://leetcode.com/problems/longest-common-subsequence/

Dados string1 e string2 você deve dizer qual a maior subsequencia que é igual.

O legal desse algoritmo é que a arvore é dificil de se enxergar a primeira vez, mas no geral é quase como house-robber, você deve definir se usa ou não a subsequencia.

Vamos ao exemplo.:

S1="abcde"
S2="ace"

A resposta desse problema é "ace", já que isso é o que é possível montar.

Vamos a outro exemplo.:

S1="ABDACDAB"
S2="ACEBFCA"

A resposta é "ABCA".

Talvez visualizando fique mais fácil. A arvore do algoritmo do primeiro caso é
```
        LCS(0,0)
           |
           |
        LCS(1,1)
          / \
         /   \
        /     \
   LCS(2,1) LCS(1,2)
```

No fim das contas esse é o algoritmo

```
         | 0                         | if i == |s1| or j == |s2| # Base Case
         |
LCS(i,j) | 1 + lcs(i+1,j+1)          | if s1[i]==s2[j]
         |
         | max(lcs(i+1,j),lcs(i,j+1) | else
````

### Top Down

A implementação com cache e usando top-down approach fica da seguinte forma

```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i,j,s1,s2,memo):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s1) or j == len(s2):
                memo[(i,j)] = 0
                return memo[(i,j)]
            elif s1[i] == s2[j]:
                memo[(i,j)] = 1 + lcs(i+1,j+1,s1,s2,memo)
                return memo[(i,j)]
            else:
                memo[(i,j)] = max(lcs(i+1,j,s1,s2,memo), lcs(i,j+1,s1,s2,memo))
                return memo[(i,j)]
        return lcs(0,0,text1,text2,{})
```

### Botoom Up

M = len(s1) + 1
N = len(s2) + 1

Comece a primeira linha e a primeira coluna com zeros. Isso vai ajudar no out-of-bounds caso

DP = [[0]*N+1 for i in range(M+1)]

O algoritmo fica assim

```
        |  1 + dp[i-1][j-1]  | if s1[i-1]==s[j-1]
DP(i,j) |
        |  max(dp[i-1][j], dp[i][j-1] | else
```

A implementação fica assim

```
def lcs(s1, s2):
    N = len(s1)
    M = len(s2)
    dp = [[0]*(M+1) for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[N][M]
```




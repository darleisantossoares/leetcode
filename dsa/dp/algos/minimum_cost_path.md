## Minimum Cost Path

Leetcode 64

https://leetcode.com/problems/minimum-path-sum/

_TL:DR_

Temos um grid NxM onde pra cada celula nos temos um preço a se pagar. Queremos ir da celula [0][0] até a última celula da direita na última linha

duas variaveis i e j

i = representa a linha

j = representa a coluna

O subproblema:
```
min_cost(i, j) = matrix[i][j] + min(min_cost(i+1, j), min_cost(i, j+1))
```

O algoritmo:
*Top Down:*
```
def minPathSum(grid):
    def cost(matrix, i, j):
        n = len(matrix)
        m = len(matrix[0])
        if i == n-1 and j == m -1:
            return matrix[i][j]
        elif i == n - 1:
            return matrix[i][j] + cost(matrix, i, j+1)
        elif i == m - 1:
            return matrix[i][j] + cost(matrix, i+1, j)
        else:
            return matrix[i][j] + min(cost(matrix, i+1, j), cost(matrix, i, j+1))

    return cost(grid, 0, 0)
```
T(n * m) = O(2n+m)

S(n * m) = O(n+m)

*Top Down With Memoization*
```
def minPathSum(grid):
    def cost(matrix, i, j, memo):
        n = len(matrix)
        m = len(matrix[0])
        if (i, j) in memo:
            return memo[(i, j)]
        if i == n-1 and j === m-1:
            return matrix[i][j]
        elif i == n-1:
            memo[(i, j)] = matrix[i][j] + cost(matrix, i, j+1, memo)
            return memo[(i, j)]
        elif j == m-1:
            memo[(i, j)] = matrix[i][j] + cost(matrix, i+1, j, memo)
            return memo[(i, j)]
        else:
            memo[(i, j)] = matrix[i][j] + min(cost(matrix,i+1,j,memo), cost(matrix,i,j+1,memo))
            return memo[(i,j)]
```
T = O(n+m)
S = O(n+m)


### The same problem with Bottom Up Approach

```
def minPathSum(grid):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0]*m for i in range(n)]
    dp[0][0] = matrix[0][0]
    for j in range(1, m):
        dp[0][j] = matrix[0][j] + dp[0][j-1]
    for i in range(1, n):
        dp[i][0] = matrix[i][0] + dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[n-1][m-1]
```

T = O(n*m)
S = O(n*m)

Podemos melhorar a questão do espaço nesse algoritmo? Sim podemos

Nesse caso vamos trabalhar somente com 2 linhas no algoritmo, nao com o grid inteiro

```
def cost(matrix):
    n, m = len(matrix), len(matrix[0])
    prev_dp = [0]*m
    dp = [0]*m
    prev_dp[0] = matrix[0][0]
    for j in range(1, m):
        prev_dp[j] = matrix[0][j] + prev_dp[j-1]
    for i in range(1, n):
        dp[0] = prev_dp[0] + matrix[i][0]
        for j in range(1, m):
            dp[j] = matrix[i][j] + min(prev_dp[j], dp[j-1])
        prev_dp = dp
        dp[0]*m
    return prev_dp[m-1]
```

S = O(m)
T = O(n*m)



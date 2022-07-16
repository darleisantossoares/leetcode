## Minimum Cost Path

Leetcode 64

https://leetcode.com/problems/minimum-path-sum/

_TL:DR_

Temos um grid NxM onde pra cada celula nos temos um preço a se pagar
Queremos ir da celula [0][0] até a última celula da direita na última linha

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


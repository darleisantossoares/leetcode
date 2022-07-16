## Unique Paths

Leetcode.: https://leetcode.com/problems/unique-paths-ii/

A melhor parte deste exercício é que a mesma lógica pode se aplicar pra qualquer problema deste mesmo tipo, seja com obstaculos ou não.

Esse problema lembra muito o anterior (minimum_cost_path)

No caso quando estamos em uma célula podemos ir pra a célula da direita ou pra a célula de baixo, em alguns casos o grid/matrix terá obstaculos.

*Base Cases*
- Out of Bounds -> return 0
- Obstaculo -> return 0
- Última célula da direita da última linha -> return 1

### Top Down Approach

```
def paths(matrix, i=0, j=0):
    n, m = len(matrix), len(matrix[0])
    if i == n or j == m or matrix[i][j] == 1:
        return 0
    elif i == n-1 and j == m-1:
        return 1
    else:
        return paths(matrix, i+1, j) + paths(matrix, i, j+1)
```

O algoritmo pode melhorar pois temos *overlapping problems* no nosso algoritmo

```
def paths(matrix, i=0, j=0, lookup=None):
    lookup = {} if lookup is None else lookup
    n, m = len(matrix), len(matrix[0])
    if (i, j) in lookup:
        return lookup[(i, j)]
    if i == n or j == m or matrix[i][j] == 1:
        return 0
    elif i == n-1 and j == m-1:
        return 1
    else:
        lookup[(i, j)] = paths(matrix, i+1, j, lookup) + paths(matrix, i, j+1, lookup)
        return lookup[(i, j)]
```

Da forma acima melhoramos um pouco a performance pois aproveitamos o que já foi computador.

### Bottom-Up

```
def paths(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [([0]*m) for i in range(n)]
    dp[0][0] = 1 if (matrix[0][0] == 0) else 0
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] if matrix[0][j] == 0 else 0
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] if matrix[i][0] == 0 else 0
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] if matrix[i][j] == 0 else 0
    return dp[n-1][m-1]
```

Ainda podemos melhorar um pouco em termos de espaço, pois só precisamos de duas rows.

```
def paths(matrix):
    n, m = len(matrix), len(matrix[0])
    prev_dp = [0]*m
    dp = [0]*m
    prev_dp[0] = 1 if (matrix[0][0] == 0) else 0
    for j in range(1, m):
        prev_dp[j] = prev_dp[j-1] if matrix[0][j] == 0 else 0
    for i in range(1, n):
        dp[0] = prev_dp[0] if matrix[i][0] == 0 else 0
        for j in range(1, m):
            dp[j] = prev_dp[j] + dp[j-1] if matrix[i][j] == 0 else 0
        prev_dp = dp
        dp = [0]*m
    return prev_dp[m-1]
```

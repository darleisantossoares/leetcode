## Bottom Up - Tabulation

Functiona como uma tabela de resultados, você vai guardando os resultados nessa tabela.

Vamos pelo exemplo de fibonacci novamente.

O número de dimensões da tabela é o mesmo número de *changing variables* no algortimo.

No exemplo de fibonacci nós só temos uma variavel que muda, então 1D array é suficiente.

Vamos ao exemplo

```
def fib(n):
    dp = [0] *(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
```

Esse acima, é o famoso *bottom-up approach*. Nesse caso o *Time Complexity* é O(n) e o *Space Complexity* é O(n).

As vezes a conseguimos melhorar o espaço utilizado pelo algoritmo.

Vamos melhorar o algoritmo acima para justamente mostrar a melhoria no uso de espaço.


```
def fib(n):
    curr, prev, before_prev = 0, 0, 0,
    before_prev = 0
    prev = 1
    for i in range(2, n+1):
        curr = prev + before_prev
        before_prev = prev
        prev = curr
    return prev
```





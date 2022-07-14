## Memoization
Normalmente para casos em que vc tem o mesmo sub problema deve-se usar memoization (cache) para optimizar a performance do algoritmo

Por exemplo no algoritmo de fibonacci

```
def fib(n)
    # Base case
    if n < 2:
        return n

    return fib(n-2) + fib(n-1)

``` 

Se analisarmos o caso acima veremos que caso ocorra uma chamada do tipo fib(10) para a função acima, a função irá computar o mesmo resultado por diversas vezes, isso é chamado de *Overlapping*

Como podemos optimizar e aproveitar esses casos em que já foram processados?
Basta grava-los em memória, e isso é a tal da *Memoization* 

O código ficaria assim

```
def fib(n, memo):
    # Memoization
    if n in memo:
        return memo[n]

    # Base case
    if n < 2:
        return n

    ans = fib(n - 2, memo) + fib(n - 1, memo)
    memo[n] = ans
    return ans
```

O código acima está aproveitando de outras interações em que já computamos um valor e o colocamos em um cache, nas próximas vezes em que formos buscar uma resposta já computada, nós simplesmente retornamos esse valor.


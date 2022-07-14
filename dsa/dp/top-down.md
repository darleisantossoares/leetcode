## Memoization
Normalmente para casos em que vc tem o mesmo sub problema deve-se usar memoization (cache) para optimizar a performance do algoritmo

Por exemplo no algoritmo de fibonacci

'''

def fib(n)
    if n < 2:
        return n

    return fib(n-2) + fib(n-1)

''' 

Se analisarmos o caso acima veremos que caso ocorra uma chamada do tipo fib(10) para a função acima, a função irá computar o mesmo resultado por diversas vezes, isso é chamado de *Overlapping*


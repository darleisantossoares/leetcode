# this is a pretty basic example of recurion without memoization
# Isso aqui pode ser considerado programacao dinamica
def fib(n):
  
    if n < 2:
        return n

    return fib(n-2) + fib(n-1)


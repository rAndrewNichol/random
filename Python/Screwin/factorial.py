def factorial(n = 0):
    if(n <= 1): return 1
    return factorial(n-1)*n

print(factorial(6))

fact = lambda x: 1 if x < 1 else x * fact(x-1)

print(fact(6))
n = 8

# to print value at nth step
def fib(n):
	if n == 0: return 0
	if n ==1: return 1
	else:
		return fib(n-1) + fib(n-2)

print("Goal: ",fib(n))

# to print recursively:
def fib_print(n, a=0, b=1):
	print(a)
	if a == fib(n):
		return 0
	return fib_print(n, b, a + b)

fib_print(n)
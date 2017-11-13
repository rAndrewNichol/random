# Closures

def closure(num):
	def mult(a):
		return num * a
	return mult

multby5 = closure(5)

print(multby5(3))
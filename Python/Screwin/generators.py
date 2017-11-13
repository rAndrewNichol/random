# Generators

# As a function:
def squares(list):
	result = []
	for i in list:
		result.append(i*i)
	return result

# As a generator
def gen_squares(list):
	for i in range(len(list)):
		yield list[i]**2

a = [1,2,3,4,5]

print(squares(a))

print(next(gen_squares(a)))
for x in gen_squares(a): print(x)
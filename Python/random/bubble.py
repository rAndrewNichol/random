x = [1,3,4,2,1,2,8,3,2,3,9,1,3]
def bubble(l):
	count = 0
	for j in reversed(range(len(l))):
		for i in range(j):
			count += 1
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
	return l, count
print(bubble(x))
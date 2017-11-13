def tri(n, i=0, summ=0):
	print(i + summ)  
	if i == n:
		return 0 
	else:
		return i + tri(n, i+1, summ + i)

tri(15)

# n = 15
# summ = 0
# for i in range(n+1):
# 	 print(i + summ)
# 	 summ = summ + i

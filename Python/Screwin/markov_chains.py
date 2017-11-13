import numpy as np

x = np.array([[.1,0,0,.4,.5,0],[.1,.2,.2,0,.5,0],[0,.1,.3,0,0,.6],[.1,0,0,.9,0,0],[0,0,0,.4,0,.6],[0,0,0,0,.5,.5]])
print(x)

y = x[:]
for i in range(100):
	y = np.matmul(y,x)

for row in y:
	print([round(x,5) for x in row])


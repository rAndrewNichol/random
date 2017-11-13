import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sci
import os

os.chdir("C:/Users/Andrew/Documents/Coding/PythonFiles/Screwin")
var = 2
mean = 5

x = np.random.uniform(size = 10000)
normal = sci.norm.ppf(x)
scaled = normal*var + mean

y = np.linspace(min(scaled) ,max(scaled) , 100)
graph = plt.hist(scaled, bins = 50, normed=True)
plt.plot(y, sci.norm.pdf(y, loc = mean, scale = var),'r-', lw=7, alpha=0.7, label='norm pdf')
plt.plot(y, sci.norm.pdf(y, loc = mean, scale = var), 'k-', lw =3, label = "frozen pdf")
plt.ylim([0,.25])
plt.savefig("normal.png", format = "png")
plt.show()

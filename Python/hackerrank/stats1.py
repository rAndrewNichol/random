# Mean, Median, Mode
# My Method
import re
import math

N = int(input())

numbers = input()
array = []
while re.search('^\s*[0-9]+', numbers) != None:
    new_entry = int(re.search('^\s*[0-9]+', numbers).group())
    numbers = re.sub('^\s*[0-9]+', "", numbers)
    array.append(new_entry)

array = sorted(array)

mean = round(sum(array)/N, 1)
print(mean)

if N % 2 == 1:
    median = round(float(array[math.floor(N/2)]),1)
else:
    lower = array[int((N/2)-1)]
    upper = array[int(N/2)]
    median = round((lower+upper)/2, 1)

print(median)

dict = {}
for x in array:
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1

temp_mode = max(dict, key = lambda i:dict[i])
find_min = []
for key in dict.keys():
    if dict[key] == dict[temp_mode]:
        find_min.append(key)

mode = min(find_min)

print(mode)

# Suggested Method (runs as python executable but not in console):
# import numpy as np
# from scipy import stats
#
# size = int(input())
# numbers = list(map(int, input().split()))
# print(np.mean(numbers))
# print(np.median(numbers))
# print(int(stats.mode(numbers)[0]))

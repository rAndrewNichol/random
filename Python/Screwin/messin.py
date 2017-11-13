x = 5 + 8
print(x)
cities = ["la", "san antonio", "san diego"]
print(cities)
dictionary = {
	"dog" : "cat",
	"frog" : "lizard"
}
print(dictionary["dog"])
dictionary["cow"] = "horse"
print(dictionary)

type(dictionary)

# let's try a nested dictionary (with lists)

majors = {
	'math': [
		'Applied Math',
		'Pure Math',
		'Statistics'
	],
	'cs': [
		'AI',
		'Software',
		'Data Science'
	]
}


print(majors)

print(majors['math'])

print(majors['math'][2])

type(True)

type(majors['math'])

majors.keys()

p = majors.values()

majors['cs'][2]

len(majors['cs'][2])

majors['cs'][2]

import numpy as np

some_numbers = [1,2,3,4,5]

print(some_numbers)

print(np.mean(some_numbers))

import pandas as pd

data = {
	'major': ['math', 'cs', 'math', 'economics'],
	'age': [18, 18, 18, 20],
	'highschool': ['svhs', 'slv', 'schs', 'pcs']
}
for key, val in data.items():
	print("My {} is {}".format(key,val))


for key in data:
	for i in range(len(data[key])):
		print("My {} is {}".format(key,data[key][i]))

for i in range(len(data['age'])):
	for key in data:
		print("My {} is {}".format(key,data[key][i]))

df_students = pd.DataFrame(data)

df_students

df_students['age']

df_students.head()

df_students[2:3]

#to index a single row
df_students.ix[2]

type(df_students.ix[2])

#selecting rows AND columns

df_students['major'][:3]

import matplotlib.pyplot as plt

print(df_students['major'].value_counts())

df_students['major'].value_counts().plot(kind='barh')

df_students.plot(kind='barh')

plt.show()

df_students.head()

df_students['major'] == 'cs'

# filter by rows where 'major' is 'math'
df_students[df_students['major']=='math']

# index by rows, and columns
#http://pandas.pydata.org/pandas-docs/stable/indexing.html
df_students.loc[:,('major','age')]
#or
df_students[['major','age']][:]

df_students[df_students['highschool'].str.contains('hs')]

df_students['highschool'][df_students['highschool'].str.contains('hs')]

#convert pandas series to python list
df_students['age'].tolist()
majors = df_students['major'].tolist()
print('math' in majors)

def major_in_list(major):
    if major in df_students['major'].tolist():
        print('yes')
    else: print('no')

major_in_list('cs')
major_in_list('art')

stem = ['cs', 'math', 'engineering']

def is_stem(major):
    if major in stem:
        return 'yes'
    elif major == 'economics':
        return 'kinda'
    else: return 'no'

print(is_stem('art'))

#applies to every major in the data frame column
df_students['major'].apply(is_stem)
type(df_students['major'].apply(is_stem))

df_students['major'].apply(is_stem).tolist()

df_students['stem'] = df_students['major'].apply(is_stem)

print(df_students)

df_students['stem'].value_counts().plot(kind='bar')
plt.show()

df_students['major_len'] = df_students['major'].apply(len)

df_students[['major_len','major']]

df_students[['major_len','major']].head(2)

for i in range(10): print(i)

list = [i for i in range(5)]
print(list)

#randomly display 2 rows of the df
df_students.sample(n=2)

df_students.sort_values(by = 'age', ascending = False)

df_students['major_len'] = df_students['major'].apply(lambda x: len(x))

#calculating percentages

#this creates a labeled array of the value counts
df_students['major'].value_counts()

df_students['major'].value_counts().values

df_students['major'].value_counts().axes

total_rows = sum(df_students['major'].value_counts())

#don't have to convert to float but maybe good practice?
percent_math = df_students['major'].value_counts()['math'] / float(total_rows)
#...

x =  1
vec = ['dog','cat','cow']

def has_pair_with_sum(vector):
	low = 0
	hi = len(vector) - 1
	while low != hi:
		if vector[low] + vector[hi] < 8:
			low += 1
		elif vector[low] + vector[hi] > 8:
			hi -= 1
		else: return True
	return False

vec1 = [1,2,3,9]
vec2 = [1,2,4,4]
has_pair_with_sum(vec1)
has_pair_with_sum(vec2)


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        raise NameError("wow you suck")
        print("Oops!  That was no valid number.  Try again...")



print(5,'\n',4)


a = [1, 2]
b = [1, 2]
c = [6, 7, a]
d = [6, 7, a]
e = a + c
f = [c, d]
a.append(5)
c[:1] = []

(3 and abs)(-1)
print(3) or 1

x = list(range(1,101))
import numpy
numpy.random.choice(x,100)


a = ['the', 'knights', 'who', 'say', 'ni']

a[1:] = ['word']

num_friends = [1,2,4]
for x,y in enumerate(num_friends):print(x,y)
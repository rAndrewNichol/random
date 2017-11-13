import re
string = ''' Sally is 15 and my friend Jill is 12. Oscar is 102. '''
ages = re.findall('\d{1,3}', string)
names = re.findall('[A-Z][a-z]*', string)
print(ages)
print(names)


d = {}
i = 0
for name in names:
	d[name] = ages[i]
	i += 1
print(d) 
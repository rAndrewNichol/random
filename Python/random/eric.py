# def asterize(string, term):
# 	return string.replace(term, '*'*len(term))

def asterize(string, term):
	build = ''
	i = 0
	while i < len(string):
		if  string[i] == term[0]:
			j = 1
			while j < len(term) and i+j < len(string):
				if string[i+j] == term[j]:
					j +=1
				else:
					break
			if j == len(term):
				build += '*'*len(term)
			else:
				build += string[i:i+j]
			i += j
		else:
			build += string[i]
			i +=1 
	return build

print asterize('catat, cat at car- ratcatc', 'cat')

def blockTerm(text, term):

	val = ''
	buf = ''
	lengthTerm = len(term) - 1
	count = 0

	for i in range(len(text)):
		if count == lengthTerm and text[i] == term[count]:
			val += '*'*(lengthTerm+1)
			buf = ''
			count = 0

		elif text[i] == term[count]:
			buf += text[i]
			count += 1

		else: 
			count = 0
			val += buf
			buf = ''
			val += text[i]

	val += buf
	return val

print blockTerm('catat, cat at car- ratcatc', 'cat')


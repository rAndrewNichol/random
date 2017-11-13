from string import ascii_lowercase
alphabet=[]
for c in ascii_lowercase:
	alphabet.append(c)
alphabet.append('a')
alphabet.append('b')
#print(alphabet)
phrase = "map"
newphrase = []
for d in phrase:
	if d.isalpha():
		for i in range(0,26):
			if d==alphabet[i]:
				newphrase.append(alphabet[i+2])
				break
	else:
		newphrase.append(d)
final = ''.join(newphrase)
print (final)

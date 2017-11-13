# File practice
import os

os.chdir("C:/Users/Andrew/Documents/Coding/PythonFiles/Screwin")
file = open("test.txt", 'w')
file.write("test first line\n")
file.write("test 2nd")
file.close()

file = open("test.txt", 'r')
print(file.read())
file.close()

file = open('test.txt', 'r')
text = file.readlines()
file.close()

import pickle

file = open("test.txt", "wb")
pickle.dump([1,2,3], file)
pickle.dump(1.2, file)
file.close()

file = open("test.txt", "rb")
x = pickle.load(file)
y = pickle.load(file)
file.close()

# Specific exception
def exists(filename):
  try:
    f = open(filename)
    f.close()
    return True
  except IOError:
    return False

# raising a value error
def inputNumber () :
  x = input ('Pick a number: ')
  if x == 17 :
    raise ValueError, '17 is a bad number'
  return x

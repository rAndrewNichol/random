import pickle
#import requests
from urllib.request import *
url = "http://www.pythonchallenge.com/pc/def/banner.p"
# source = requests.get(url).text
data = pickle.load(urlopen(url))
for line in data:
	print("".join([char * times for (char, times) in line]))

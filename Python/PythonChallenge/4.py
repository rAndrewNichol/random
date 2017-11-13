import re
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
text = str(requests.get(url).content)

while(re.search('and the next nothing is', text)):
	next_num = re.findall('and the next nothing is ([0-9]+)', text)[0]
	print(next_num)
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + next_num
	text = str(requests.get(url).content)


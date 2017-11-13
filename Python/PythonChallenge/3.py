import requests
import re
url = "http://www.pythonchallenge.com/pc/def/equality.html"
source = requests.get(url)
string = str(source.content).replace(" ", "")
matches = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", string)
print(matches)

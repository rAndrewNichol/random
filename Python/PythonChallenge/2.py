# Grabbing page source:
import requests
import re
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
source = requests.get(url)
#print(str(source.content))
letters = re.findall("(?!n)[a-zA-Z]+", str(source.content))
print(letters)
# equality.... 
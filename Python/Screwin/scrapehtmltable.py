import pandas as pd
import numpy as np
import bs4 as bs
import requests

url = "http://www.basketball-reference.com/teams/CLE/2016.html"
html = requests.get(url)
bs = bs.BeautifulSoup(html.content, 'lxml')
table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="roster")
rows = table.findAll(lambda tag: tag.name=='tr')
table= str(table)
print(table)
# print(type(table))
# df = pd.read_html(table)
# print(df)


# doesn't work because table is commented out in the source.
# table2 = bs.find(lambda tag: tag.name =='table' and tag.has_attr('id') and tag['id'] == "totals")
# table2 = str(table2)
# df2 = pd.read_html(table2)

# so we can grab it manually.
string = str(bs)
begin = string.find('<div class="overthrow table_container" id="div_totals">')
tranche = string[begin:]
table2 = tranche[ : tranche.find('</table')+ 7]
# print(table2)
df2 = pd.read_html(table2)
print(df2)


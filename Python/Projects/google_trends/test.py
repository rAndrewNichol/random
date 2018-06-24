from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["blockchain"]
pytrends.build_payload(kw_list, cat=0, timeframe='now 1-d', geo='', gprop='')
df = pytrends.interest_over_time()
print(df)
df = pytrends.trending_searches()
print()
print(df)
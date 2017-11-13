f# This program queries some information from the web. It grabs the html source of various sites
# and does some basic parsing manipulation to extract information about stocks based on their ticker synbols.

import urllib.request as request
import re

def get_company(ticker):
    # This function uses modules 'requests' and 'beautiful soup' to extract the name of the corporation that is
    # represented by the input ticker symbol. This function queries money.cnn.com
    import requests
    import bs4 as bs
    url = "http://money.cnn.com/quote/quote.html?symb=" + ticker
    source = requests.get(url)
    soup = bs.BeautifulSoup(source.content, 'lxml')
    return soup.find("h1").contents[0]

def find_exchange(ticker):
    # This function uses only urllib.request to query finance.yahoo.com and find the exchange market which trades
    # the requested stock.
    url = 'https://finance.yahoo.com/quote/' + ticker
    html = str(request.urlopen(url).read())
    begin = html.find('reactid="244"')
    # This if/elif uses the base function str.find() to determine whether the stock (based on ticker symbol)
    # is traded on the Nasdaq or the NYSE.
    if html[begin:begin+50].find("Nasdaq") != -1:
        return "Nasdaq"
    elif html[begin:begin+50].find("NYSE") != -1:
        return "New York Stock Exchange"
    else: return None

# Price/Earning Ratio
def get_barrons_per(html):
    # This function uses base Python string parsing and a basic regular expression function to extract the price
    # earnings ratio of the requested security. The expected input is the html source of an individual stock
    # page from barrons.com
    begin = html.find("P/E Ratio")
    tranche = html[begin:]
    PER = re.search('[0-9]*\.[0-9]+', tranche).group()
    return PER

# Latest price
def get_price(html):
    # Same as the last function but locates the most recent price close from barrons.com htmnl source.
    begin = html.find("Previous Close")
    tranche = html[begin:]
    price = re.search('[0-9]*\.[0-9]+', tranche).group()
    return '$' + price

def market_dict(x):
    # Basic keyed dictionary to translate the syntax used to locate securities by exchange market on barrons.com
    return {
        'Nasdaq' : 'nas',
        'New York Stock Exchange' : 'nys'
    }[x]

# Input loop that breaks upon user prompt.
while True:
    symbol = input("Ticker symbol or (e)xit: ")
    if symbol == 'e': print("Thanks for trying!"); break
    try:
        # find exchange from yahoo finance
        market = find_exchange(symbol)
        # grabs source html from barrons.com using the exchange market (syntax converted) and our ticker from input
        url = "http://www.barrons.com/quote/stock/us/x" + market_dict(market) + '/' + symbol
        source = request.urlopen(url)
        source_page = str(source.read())
        # print the company name from money.cnn.com
        print(get_company(symbol))
        print(market)
        print("Price (last close):", get_price(source_page))
        print("Price/Earnings Ratio:", get_barrons_per(source_page), '\n')
        source.close()
    except: print("Ticker not found, please try again.")


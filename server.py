from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 


@route('/')
def index():

	URL = "http://public.mig.kz/"

	resp = requests.get(URL)
	bs4 = BeautifulSoup(resp.content, "html.parser")
	rubBuy = None
	rubSell = None
	usdBuy = None
	usdSell = None
	eurBuy = None
	eurSell = None
	for tag in bs4.find_all('td', class_ = 'currency'):
		if tag.string == 'USD':
			buy = tag.parent.find_all('td', class_ = 'buy')
			sell = tag.parent.find_all('td', class_ = 'sell')
			usdBuy = buy[0].string
			usdSell = sell[0].string
		if tag.string == 'RUB':
			buy = tag.parent.find_all('td', class_ = 'buy')
			sell = tag.parent.find_all('td', class_ = 'sell')
			rubBuy = buy[0].string
			rubSell = sell[0].string
		if tag.string == 'EUR':
			buy = tag.parent.find_all('td', class_ = 'buy')
			sell = tag.parent.find_all('td', class_ = 'sell')
			eurBuy = buy[0].string
			eurSell = sell[0].string

	return {"usd": usdSell, "eur": eurSell, "rub": rubSell}


URL = "https://github.com/giAtSDU/apt_spring_2016_hw1"

@route('/forks')
def forks():
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")
    res = None
    for tag in bs4.find_all('a'):
        if tag.has_attr('class') and 'social-count' in tag.attrs['class']:
            res = int(tag.string)
    return {"forks": res}

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

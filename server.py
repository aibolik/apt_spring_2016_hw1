from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 


@route('/')
def index():

	URL = "http://public.mig.kz/"

	resp = requests.get(URL)
	bs4 = BeautifulSoup(resp.content, "html.parser")
	rub = None
	usd = None
	eur = None
	for tag in bs4.find_all('h4'):
		if tag.string == 'usd':
			p = tag.parent.p.string
			usd = p.split(' ')[0]
		if tag.string == 'rub':
			p = tag.parent.p.string
			rub = p.split(' ')[0]
		if tag.string == 'eur':
			p = tag.parent.p.string
			eur = p.split(' ')[0]

	return {"usd": usd, "eur": eur, "rub": rub}


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

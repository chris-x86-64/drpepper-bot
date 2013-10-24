# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def check_price(target_url):
	content = urllib.urlopen(target_url)
	parser = BeautifulSoup(content)
	price = filter(
		lambda x: x.isdigit(),
		parser.findAll('b', {'class':'priceLarge'})[0].contents[0].strip()
	)
	print price

if __name__ == '__main__':
	try:
		check_price('http://www.amazon.co.jp/dp/B001U7651A/')
	except:
		raise

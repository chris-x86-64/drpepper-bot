# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def check_item(target):
	content = urllib.urlopen(target['url'])
	parser = BeautifulSoup(content)

	price_str = parser.findAll('b', {'class':'priceLarge'})[0].contents[0].strip()
	price = int(filter(lambda x: x.isdigit(), price_str))

	return {'item': target, 'price': {'str': price_str, 'int': price}}

if __name__ == '__main__':
	try:
		print check_item({'name':'500mlペット*24本', 'url': 'http://www.amazon.co.jp/dp/B001U7651A/'})
	except:
		raise

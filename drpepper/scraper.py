# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def check_item(target):
	content = urllib.urlopen(target['url'])
	parser = BeautifulSoup(content)

	price_str = parser.findAll('b', {'class':'priceLarge'})[0].contents[0].strip()
	price = int(filter(lambda x: x.isdigit(), price_str))

	return {'item': target, 'price': {'str': price_str, 'int': price}}

def test():
	import yaml

	items = yaml.load(open("config.yml"))['items']

	for item in items:
		try:
			print check_item(item)
		except:
			raise

if __name__ == '__main__':
	test()

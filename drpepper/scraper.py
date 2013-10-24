# -*- coding: utf-8 -*-

from beautifulscraper import BeautifulScraper

def check_price(target_url):
	scraper = BeautifulScraper()
	content = scraper.go(target_url)
	price = filter(
		lambda x: x.isdigit(),
		content.findAll('b', {'class':'priceLarge'})[0].contents[0].strip()
	)
	print price

if __name__ == '__main__':
	check_price('http://www.amazon.co.jp/Dr-Pepper-%E3%83%89%E3%82%AF%E3%82%BF%E3%83%BC%E3%83%9A%E3%83%83%E3%83%91%E3%83%BC-3422-%E3%83%89%E3%82%AF%E3%82%BF%E3%83%BC%E3%83%9A%E3%83%83%E3%83%91%E3%83%BC500ml%C3%9724%E6%9C%AC/dp/B001U7651A')

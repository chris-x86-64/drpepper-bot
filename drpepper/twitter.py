# -*- coding: utf-8 -*-

import yaml
import tweepy
from datetime import datetime
from string import Template

def prepare_api():
	keys = yaml.load(open("config.yml"))['oauth']

	oauth = tweepy.OAuthHandler(keys['consumer']['key'], keys['consumer']['secret'])
	oauth.set_access_token(keys['access_token']['key'], keys['access_token']['secret'])

	return tweepy.API(auth_handler = oauth, secure = True, retry_count = 3)

def post(item, price):
	now = datetime.now().strftime("%Y/%m/%d %H:%M")
	status = Template(
		u'${date_and_time} 現在の ${item} の価格: ${price} (前日比 ${diff}) ${url}'
		).substitute(
			{'date_and_time': now, 'item': item, 'price': price, 'diff': 0, 'url': 'nanka'}
		)
	return status

def test():
	api = prepare_api()
	print post(u'なんか', u'￥ 100')
	try:
		print api.me().__dict__
	except:
		raise

if __name__ == '__main__':
	test()

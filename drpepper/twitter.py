# -*- coding: utf-8 -*-

import yaml
import tweepy
from datetime import datetime
from string import Template

def _prepare_api():
	keys = yaml.load(open("config.yml"))['oauth']

	oauth = tweepy.OAuthHandler(keys['consumer']['key'], keys['consumer']['secret'])
	oauth.set_access_token(keys['access_token']['key'], keys['access_token']['secret'])

	return tweepy.API(auth_handler = oauth, secure = True, retry_count = 3)

def post(data):
	now = datetime.now().strftime("%Y/%m/%d %H:%M")
	status = Template(
		u'${date_and_time} 現在の ${item} の価格: ${price} (前日比 ${diff}) ${url}'
		).substitute(
			{'date_and_time': now, 'item': data['item']['name'], 'price': data['price']['str'], 'diff': None, 'url': data['item']['url']}
		)
	api = _prepare_api()
	api.update_status(status)

def test():
	items = yaml.load(open("config.yml"))['items']
	api = _prepare_api()

	for item in items:
		print post(item, {'str': u'￥ 100', 'int': 100})
	try:
		print api.me().__dict__
	except:
		raise

if __name__ == '__main__':
	test()

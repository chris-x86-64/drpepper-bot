# -*- coding: utf-8 -*-

import yaml
import tweepy

def prepare_api():
	keys = yaml.load(open("config.yml"))['oauth']

	oauth = tweepy.OAuthHandler(keys['consumer']['key'], keys['consumer']['secret'])
	oauth.set_access_token(keys['access_token']['key'], keys['access_token']['secret'])

	return tweepy.API(auth_handler = oauth, secure = True, retry_count = 3)

def test():
	api = prepare_api()
	try:
		print api.me().__dict__
	except:
		raise

	try:
		api.update_status(u'てすてす')
	except:
		raise

if __name__ == '__main__':
	test()

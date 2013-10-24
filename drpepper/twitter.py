# -*- coding: utf-8 -*-

import yaml
import tweepy

def prepare_api():
	config = yaml.load(open("config.yml"))

	class Keys(object):
		class consumer(object):
			key = config['oauth']['consumer']['key']
			secret = config['oauth']['consumer']['secret']
		class access_token(object):
			key = config['oauth']['access_token']['key']
			secret = config['oauth']['access_token']['secret']

	oauth = tweepy.OAuthHandler(Keys.consumer.key, Keys.consumer.secret)
	oauth.set_access_token(Keys.access_token.key, Keys.access_token.secret)

	return tweepy.API(auth_handler = oauth, secure = True, retry_count = 3)

def test():
	api = prepare_api()
	print api.me().__dict__

if __name__ == '__main__':
	test()

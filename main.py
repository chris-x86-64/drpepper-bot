#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import yaml

config = yaml.load(open("config.yml"))

class Keys():
	keys = config['oauth']
	class consumer():
		key = keys['consumer']['key']
		secret = keys['consumer']['secret']
	class access_token():
		key = keys['access_token']['key']
		secret = keys['access_token']['secret']

def main():
	print Keys.consumer.key

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import yaml

config = yaml.load(open("config.yml"))

class Keys(object):
	class consumer(object):
		key = config['oauth']['consumer']['key']
		secret = config['oauth']['consumer']['secret']
	class access_token(object):
		key = config['oauth']['access_token']['key']
		secret = config['oauth']['access_token']['secret']

def main():
	print Keys.consumer.key

if __name__ == '__main__':
	main()

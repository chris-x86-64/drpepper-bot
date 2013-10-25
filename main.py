#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import drpepper.scraper
import drpepper.twitter
import yaml

def main():
	items = yaml.load(open("config.yml"))['items']

	for item in items:
		drpepper.twitter.post(
			drpepper.scraper.check_item(item)
		)

if __name__ == '__main__':
	main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep

import re
import sys
import requests
import urllib.request
import random
import argparse

good = "\033[92m✔\033[0m"

# This magic spell lets me erase the current line. 
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where 
# "Downloading..." was.  
ERASE_LINE = '\x1b[2K'

# This extracts the video url
def extract_url(html, quality):

	if quality == "sd":
		# Standard Definition video
		url = re.search('sd_src:"(.+?)"', html)[0]
	else:
		# High Definition video
		url = re.search('hd_src:"(.+?)"', html)[0]

	# cleaning the url 
	url = url.replace('hd_src:"', '')
	url = url.replace('sd_src:"', '')
	url = url.replace('"', "")

	return url


def main():
	parser = argparse.ArgumentParser(description = "Download videos from facebook from your terminal")
	
	parser.add_argument('url', action="store")
	parser.add_argument('resolution', action="store", nargs="?")

	args = parser.parse_args()

	print("Fetching source code...", end="\r", flush=True)
	r = requests.get(args.url)
	sys.stdout.write(ERASE_LINE)
	print(good, "Fetched source code")

	file_url = extract_url(r.text, args.resolution)

	# Generates a random number with will be the file name
	path = str(random.random())[3:12] + ".mp4"

	print("Downloading video...",  end="\r", flush=True)
	# Downloads the video
	urllib.request.urlretrieve(file_url, path)
	sys.stdout.write(ERASE_LINE)
	print(good, "Video downloaded:", path)

if __name__=="__main__":
	main()
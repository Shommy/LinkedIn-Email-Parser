#!/usr/bin/python

import sys
import os

usage = """

********************************************************
_____ _          ____                                 
|_   _| |__   ___|  _ \ _ __ ___ _ __  _ __   ___ _ __ 
  | | | '_ \ / _ \ |_) | '__/ _ \ '_ \| '_ \ / _ \ '__|
  | | | | | |  __/  __/| | |  __/ |_) | |_) |  __/ |   
  |_| |_| |_|\___|_|   |_|  \___| .__/| .__/ \___|_|   
                                |_|   |_|              

********************************************************

The script takes the list of names from the file or it uses harvester to grab the list from the LinkedIn.

It then creates the list of email addresses.

Usage:

./theprepper.py <email_domain> <mode> <optional_names_file>

modes:

1 - <first_initial><last_name>@domain (default)
2 - <first_name><last_initial>@domain
3 - <first_name>.<last_name>@domain
4 - <first_name><last_name>@domain

Examples:

./theprepper.py somecompany.com 1 
./theprepper.py somecompany.com 2 full_names.txt


"""

def main(args):
	if len(args) < 2:
		print usage
		sys.exit(1)

	domain = args[0]
	mode = int(args[1])

	if len(args) > 2:
		in_file = open(args[2])
		for line in in_file.readlines():
			print make_email(line, domain, mode)
		in_file.close()
	else:
		harvester_output = os.popen("theharvester -d " + domain + " -l 1000 -b linkedin").read()
		names_start = False

		for line in harvester_output.split('\n'):
			if line.startswith("===="):
				names_start = True
				continue
			if names_start and line:
				print make_email(line, domain, mode)

def make_email(line, domain, mode):
	words = line.strip().split()
	if mode == 4:
		username = words[0].lower() + words[len(words)-1].lower()
	elif mode == 3:
		username = words[0].lower() + "." + words[len(words)-1].lower()
	elif mode == 2:
		username = words[0].lower() + words[len(words)-1].lower()[0]
	else: # 1 and default
		username = words[0].lower()[0] + words[len(words)-1].lower()

	return username + "@" + domain

if __name__ == "__main__" : main(sys.argv[1:])

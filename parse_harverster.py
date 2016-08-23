#!/usr/bin/python

import sys
import os

usage = """
Usage:

./parse.py <email_domain> <mode>

modes:

1 - <first_initial><last_name>@domain (default)
2 - <first_name><last_initial>@domain
3 - <first_name>.<last_name>@domain
4 - <first_name><last_name>@domain

"""

def main(args):
	if len(args) < 2:
		print usage
		sys.exit(1)

	domain = args[0]
	mode = int(args[1])

	harvester_output = os.popen("theharvester -d " + domain + " -l 1000 -b linkedin").read()
	names_start = False

	for line in harvester_output.split('\n'):
		if line.startswith("===="):
			names_start = True
			continue
		if names_start and line:
			words = line.split()
		
			if mode == 4:
				username = words[0].lower() + words[len(words)-1].lower()
			elif mode == 3:
				username = words[0].lower() + "." + words[len(words)-1].lower()
			elif mode == 2:
				username = words[0].lower() + words[len(words)-1].lower()[0]
			else: # 1 and default
				username = words[0].lower()[0] + words[len(words)-1].lower()

			email = username + "@" + domain
			print email

if __name__ == "__main__" : main(sys.argv[1:])

#!/usr/bin/python

import sys

usage = """
Usage:

./parse.py <file_with_linkedin_names> <email_domain> <mode>

modes:

1 - <first_initial><last_name>@domain (default)
2 - <first_name><last_initial>@domain
3 - <first_name>.<last_name>@domain
4 - <first_name><last_name>@domain

"""

def main(args):
  if len(args) < 3:
  	print usage
  	sys.exit(1)

  inFile = open(args[0])
  domain = args[1]
  mode = int(args[2])
  for line in inFile.readlines():
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
  inFile.close()

if __name__ == "__main__" : main(sys.argv[1:])

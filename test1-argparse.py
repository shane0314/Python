#!/usr/bin/python
import argparse
import sys
import os
import time

def main():
	parser = argparse.ArgumentParser( description = "A test argparse",
		epilog = "[example] python test1-argparse.py -f myfilename --flag -n Tome Tony Tim -a 18 --age 20 --age 34",
		prog = "test-argparse")
	
	# suport a short and long version of a required argument using lile '"-f", "--foo"'
	# requried = Ture means the option must be provided
	parser.add_argument("-f","--file", dest = "file", help = "configure file", required = True )
	# nargs = "+", the option accept several arguments, --names Tom Jack Nana 
	parser.add_argument("-n","--names", dest = "names", nargs = "+", help = "multi names", type = str)
	# action = "append", multipe options's arguments are appended, --age 18 20 21
	parser.add_argument("-a","--age", dest = "age", action = "append", help = "multi age", type = int)
	# bool not args after the option
	parser.add_argument("--flag", dest = "flag", help = "print args", action = "store_true")
	
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)

	args = parser.parse_args()
	if args.flag:
		print(args)
	if args.file:
		print args.file
	if args.names:
		print args.names
	if args.age:
		print args.age

	print "test end"
		
if __name__ == "__main__":
    main()

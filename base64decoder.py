#!/usr/bin/python
import base64
import argparse

parser = argparse.ArgumentParser(description='Enter CAL Response file name.')
parser.add_argument("fileName")
parser.add_argument("option")
args = parser.parse_args()
with open(args.fileName) as f:
	output = open('output.txt', 'w')
	content = f.readlines()
	for i in range(len(content)):
		if args.option.lower() == 'encode':
			output.write(base64.encodestring(content[i]))
		else:
			output.write(base64.decodestring(content[i]))
	output.close()
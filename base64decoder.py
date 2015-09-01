#!/usr/bin/python
import base64
import argparse

parser = argparse.ArgumentParser(description='Enter CALResponse file name.')
parser.add_argument("fileName")
args = parser.parse_args()
with open(args.fileName) as f:
	output = open('output.txt', 'w')
	content = f.readlines()
	for i in range(len(content)):
		output.write(base64.decodestring(content[i]))
	output.close()
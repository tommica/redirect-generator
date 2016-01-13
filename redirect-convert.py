#!/user/bin/python

import time
import csv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file", help="Give the path to the file")
parser.add_argument("delimiter", help="CSV delimiter character", default=",")
parser.add_argument("enclosure", help="CSV enclosure character", default='"')

args = parser.parse_args()

timestamp = int(time.time())
filename = 'output_' + str(timestamp) + '.txt'

rownum = 0
with open(filename, 'w') as text_file:
	with open(args.file, 'rb') as f:
		reader = csv.reader(f, delimiter=args.delimiter, quotechar=args.enclosure)
		for row in reader:
			if rownum > 0:
				result = 'Redirect 301 ' + str(row[0]) + str(' ') + str(row[1]) + str('\n')
				text_file.write(result)
			rownum += 1

import re

first_nice_string = re.compile("([a-z][a-z]).*\\1")
second_nice_string = re.compile("([a-z])[a-z]\\1")

with open('day5.txt') as f:
	print len([l for l in f if first_nice_string.search(l) and
				second_nice_string.search(l)])
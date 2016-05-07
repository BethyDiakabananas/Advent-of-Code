import re

first_nice_string = re.compile('(.*[aeiou].*){3,}')
second_nice_string = re.compile("([a-z])\\1")
bad_string = re.compile("ab|cd|pq|xy")

with open('day5.txt') as f:
	print len([l for l in f
				if (not bad_string.search(l)) and
				first_nice_string.search(l) and
				second_nice_string.search(l)])
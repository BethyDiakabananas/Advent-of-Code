#Day One Solution
with open('day1.txt') as file:
	print sum(1 if parenthesis == '(' else -1
				for parenthesis in file.read().strip())

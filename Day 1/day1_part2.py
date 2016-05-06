floor = 0
with open('day1.txt') as f:
	for i, parenthesis in enumerate(f.read(), 1):
		if parenthesis == '(':
			floor += 1
		if parenthesis == ')':
			floor -=1
		if floor < 0:
			break
print i
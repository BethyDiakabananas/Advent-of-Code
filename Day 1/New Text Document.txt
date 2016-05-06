file = open('Day1.txt', 'r')
up, down = 0, 0
while True:
	parenthesis = file.read(1)
	if parenthesis == '(':
		up += 1
	elif parenthesis == ')':
		down += 1
	else:
		break
print up - down


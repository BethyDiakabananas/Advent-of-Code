total = 0
with open('day2.txt') as f:
	for line in f:
		l, w, h = map(int, line.split('x'))
		total += l * w * h
		total += 2 * (l + w + h - max(l, w, h))
print total




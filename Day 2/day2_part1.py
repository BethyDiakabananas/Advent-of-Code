area = 0
with open('day2.txt') as f:
	for line in f:
		l, w, h = map(int, line.split('x'))
		surface_area = (2*l*w) + (2*w*h) + (2*h*l)
		slack = min((l*w), (w*h), (h*l))
		area += surface_area + slack
print area




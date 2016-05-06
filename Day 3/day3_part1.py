x, y = 0, 0
visited_houses = set([(x, y)])
with open('day3.txt') as f
	for move in f.read().strip():
		if move == '^':
			y += 1
		elif move == '>':
			x += 1
		elif move == '<':
			x -= 1
		elif move == 'v':
			y -= 1
		visited_houses.add((x,y))
print len(visited_houses)

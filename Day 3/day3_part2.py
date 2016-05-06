santas = 2
coordinates = [(0,0)] * santas
visited_houses = set([0,0])

with open('day3.txt') as f:
	moves = f.read()
	arrows = [moves[i:i+santas] for i in xrange(0, len(moves), santas)]
	for arrow in arrows:
		for i, move in enumerate(arrow):
			x, y = coordinates[i]
			if move == '^':
				y += 1
			elif move == '>':
				x += 1
			elif move == '<':
				x -= 1
			elif move == 'v':
				y -= 1
			visited_houses.add((x,y))
			coordinates[i] = (x, y)
print len(visited_houses) 

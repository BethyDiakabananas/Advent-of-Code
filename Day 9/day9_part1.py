from itertools import permutations

distances = {}
places = set()

with open('day9.txt') as f:
	for line in f:
		pieces = line.split(' ')
		frm, _, to, _, amount = pieces
		amount = int(amount.strip())
		distances[frm, to] = distances[to, frm] = amount
		places.add(frm)
		places.add(to)

possible_routes = permutations(places)
total_distances = []

for route in possible_routes:
	total = 0
	for i, frm in enumerate(route):
		if i == len(route) - 1:
			break
		to = route[i+1]
		total += distances[(frm, to)]
	total_distances.append(total)

print min(total_distances)
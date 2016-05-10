with open('day8.txt') as f:
	print(sum([line.strip().count('\\') + line.strip().count('"') + 2 for line in f]))		
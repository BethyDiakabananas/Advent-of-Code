with open('day8.txt') as f:
	print(sum([len(line.strip()) - len(eval(line)) for line in f]))
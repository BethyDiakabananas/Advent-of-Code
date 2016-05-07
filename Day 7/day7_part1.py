import re
find_commands = re.compile("[A-Z]+")
find_args = re.compile("[a-z0-9]+")

functions = {
	'AND': lambda a,b: a & b,
	'OR': lambda a,b: a | b,
	'LSHIFT': lambda a,b: a << b,
	'RSHIFT': lambda a,b: a >> b,
	'NOT': lambda a: ~a,
}

def resolve(symbol):
	if isinstance(symbol, int):
		return symbol
	value = wires[symbol]
	if not isinstance(value, tuple):
		return value

	command, args = value
	if not command:
		result = resolve(args[0])
		wires[symbol] = result
		return result
	else:
		resolved_args = [resolve(x) for x in args]
		result = functions[command](*resolved_args)
		wires[symbol] = result
		return result

wires = {}
with open('day7.txt') as f:
	for line in f:
		command = find_commands.search(line)
		args = find_args.findall(line)
		args = [int(x) if x.isdigit() else x for x in args]
		if command:
			command = command.group()
		to_wire = args.pop()
		wires[to_wire] = (command, tuple(args))

print resolve('a')
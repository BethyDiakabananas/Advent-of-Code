import re 

input = '1113122113'
repeated_digits = re.compile(r'((\d)\2*)')

for i in range(0, 40):
	temp_input = ''
	for match, number in repeated_digits.findall(input):
		temp_input += str(len(match))
		temp_input += number
	input = temp_input
print(len(input))

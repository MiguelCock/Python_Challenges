colors = ["R", "G", "B", "Y"]

lights = input()
pattern = ['', '', '', '']

for i in range(len(lights)):
	pos = i - (i//4)*4
	if lights[i] in colors:
		pattern[pos] = lights[i]

dicc = {'R':0, 'G':0, 'B':0, 'Y':0}

for i in range(len(lights)):
	pos = i - (i//4)*4
	if lights[i] == '!':
		dicc[pattern[pos]] += 1

print(dicc)
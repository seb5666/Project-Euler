# returns a list of all rotations of the integer number n #
def rotations(n):
	rotations = [n]
	string = str(n)
	if len(string) == 1:
		return rotations

	strlength = len(string)

	for i in range(0,strlength-1):
		first = string[0]
		new = ""
		for j in range(1,strlength):
			new += string[j]
		new += first
		string = new
		r = int(new)
		if r not in rotations:
			rotations.append(int(new))

	return rotations

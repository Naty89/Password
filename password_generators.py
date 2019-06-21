def password():
	numbers = []
	uppercase = []
	symbols = []
	lowercase = []
	c = []
	a = ["welcom","abc123","password6543","password1234","123456", "123456789101"]
	for i in range(33, 127):
		c.append(chr(i))
	for l in range(len(c)-1):
		numbers.append(c[])
		uppercase.append(c[])
		symbols.append(c[])
		lowercase = (c[])
	i = raw_input("Pick hard or easy password in lowercase:")
	r = raw_input("Pick length of password 6 or 12:")
	o = int(r)
	if i == "hard":
		from random import shuffle
		for k in range(len(c)-1):
			shuffle(c)
			m = "".join(c[0:o+1])
		return m
	if i == "easy":
		for m in range(len(a)-1):
			if len(a[m]) == o:
				h.append(a[m])
				from random import choice
				x = choice(h)
				return x

print(password())	


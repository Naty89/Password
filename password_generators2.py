def password():
	c = []
	a = ["welcome","abc123","password","password1","12345", "12345678"]
	for i in range(33, 128):
		c.append(chr(i))
	i = raw_input("Pick hard or easy password in lowercase:")
	if i == "hard":
		from random import shuffle
		for k in range(len(c)-1):
			shuffle(c)
			m = "".join(c[0:11])
		return m
	if i == "easy":
		from random import choice
		x = choice(a)
		return x

print(password())	

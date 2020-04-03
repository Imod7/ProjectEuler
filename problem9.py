# Problem 9 : Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_odd(num):
	if (num % 2 == 0):
		return (0)
	else:
		return (1)

def square_num(n):
	return (n * n)

def pyth_tripl(init):
	if (is_odd(init) == 1):
		a = init * init
		a = int(a / 2)
		b = a + 1
	if (is_odd(init) == 0):
		a = int(init / 2)
		a = a * a
		b = a + 1
		a = a - 1
	return init, a, b, 

def mult_triplets(a, b, c):
	i = 2
	sum = a*i + b*i + c*i
	while sum <= 1000:
		if (a*i + b*i + c*i) == 1000:
			print("final triplet is", a*i*b*i*c*i)
			return (1)
		i += 1
		sum = a*i + b*i + c*i
	return (0)

i = 3
sum = 0
while sum <= 1000:
	a, b, c = pyth_tripl(i)
	if ((square_num(a) + square_num(b)) == square_num(c)):
		# print("the triplet is", a, b, c)
		sum = a + b + c
		if (sum == 1000):
			print("final triplet is", a*b*c)
			break
		if (mult_triplets(a, b, c) == 1):
			break
	i += 1
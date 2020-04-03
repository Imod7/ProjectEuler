# Problem 3 : Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_num(num):
	i = 2
	while i < num:
		if (num % 2 == 0):
			return (0)
		i += 1
	return (1)

num = 600851475143
# num = 228

div = 2
list = []
while num > 2:
	# print("num = ", int(num))
	# print("prime :", div)
	while (num % div != 0):
		div = div + 1
		while (prime_num(div) == 0):
			div = div + 1
		break
	else:
		print("next prime :", div)
		list.append(div)
		num = int(num / div)

print("largest prime factor :", list[-1])

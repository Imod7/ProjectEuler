# Problem 5 : Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

finalist = []

def prime_num(num):
	i = 2
	while i < num:
		if (num % 2 == 0):
			return (0)
		i += 1
	return (1)

def prime_factors(num):
	templ = []
	div = 2
	while num >= 2:
		if (num % div != 0):
			div = div + 1
			while (prime_num(div) == 0):
				div = div + 1
		else:
			num = num / div
			templ.append(div)
	return templ

i = 1
while i <= 20:
	temp = []
	# print("num = ", i)
	temp = prime_factors(i)
	# print("prime factors :", temp)
	temp.sort()
	for j in temp:
		if j in finalist:
			# print("exists num = ", j)
			if (finalist.count(j) < temp.count(j)):
				dif = temp.count(j) - finalist.count(j)
				k = 0
				while k < dif:
					finalist.append(j)
					k += 1
		else:
			# print("doesnt exist num = ", j)
			finalist.append(j)
	# print("final factors :", finalist)
	finalist.sort()
	i += 1

prod = 1
for k in finalist:
	prod = prod * k
	# print(prod)
print("Final result : ", prod)
# Problem 7 : 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

mylist = []

def prime_num(num):
	i = 2
	div = 2
	while i < num:
		# print(i)
		if (num % div == 0):
			return (0)
		i += 1
		div = div + 1
	return (1)

def program():
	i = 2
	while (len(mylist) != 10001):
		if (prime_num(i) == 1):
			mylist.append(i)
		i += 1
		print("len list : ", len(mylist), "/10001")

program()
# print(mylist)
print("the 10001st prime :", mylist[10000])
# Problem 2 : Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def fib(a, b):
	temp = a + b
	b = temp + b
	return (temp, b)

i = 0
a = 1
b = 2
sum = 0
while i < 4000000:
	# print(a)
	# print(b)
	if (a % 2 == 0):
		sum = sum + a
	if (b % 2 == 0):
		sum = sum + b
	# print("sum = ", sum)
	a, b = fib(a, b)
	i += a

print("final sum = ", sum)

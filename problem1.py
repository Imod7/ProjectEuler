# Problem 1 : Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiple(num):
	if ((num % 3 == 0) or (num % 5 == 0)):
		return (1)
	else:
		return (0)

sum = 0
i = 0
while i < 1000:
	if multiple(i) == 1:
		sum = sum + i
	i += 1

print (sum)
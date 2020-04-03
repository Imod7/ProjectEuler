# Problem 6 : Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

def sum_squares(num):
	i = 1
	sum = 0
	while i <= num:
		j = i * i
		sum = sum + j
		i += 1
	return (sum)

def square_sum(num):
	i = 1
	sum = 0
	while i <= num:
		sum = sum + i
		i += 1
	sum = sum * sum
	return (sum)

def program(num):
	sum_sq = sum_squares(num)
	sq_sum = square_sum(num)
	print("sum squares = ", sum_sq)
	print("square of sums = ", sq_sum)
	print("dif = ", sq_sum - sum_sq)

program(100)
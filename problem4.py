# Problem 4 : Largest palindrome product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palind(num):
	mystr = str(num)
	revstr = mystr[::-1]
	if (mystr == revstr):
		return (1)
	return (0)

def check_j(i):
	j = 999
	while j > 800:
		product = i * j
		if (check_palind(product) == 1):
			return (product)
		j -= 1
	return (0)

i = 999
prod = 0
mylist = []
while i > 800:
	if (check_j(i) != 0):
		prod = check_j(i)
		mylist.append(prod)
	i -= 1

print("max pal", max(mylist))
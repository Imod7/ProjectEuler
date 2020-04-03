# Problem 8 : Largest product in a series
# The four adjacent digits in the 1000-digit number that have the greatest product
# are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

with open('problem8_input.txt', 'r') as file:
    data = file.read().replace('\n', '')

mylist = []
for elem in data:
	mylist.append(int(elem))

# print(mylist)

def find_prod(lst):
	prod = 1
	# print(lst)
	for elem in lst:
		prod = prod * elem
	# print (prod)
	return (prod)

def program(num):
	i = 0
	max = num
	result = 0
	length = len(mylist[i:max])
	while num == length:
		res = find_prod(mylist[i:max])
		if (res > result):
			result = res
		i += 1
		max += 1
		length = len(mylist[i:max])
		# print(length)
	print("final result = ", result)

program(13)

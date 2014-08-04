numbers = []

def appendNumbersUpTo(x, y):
	i = 0
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)
		i += y
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

def appendNumbersUpTo2(x, y):
	for i in range(0, x, y):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i




appendNumbersUpTo(6, 2)
appendNumbersUpTo2(6, 2)

print "The numbers: "

for num in numbers:
	print num
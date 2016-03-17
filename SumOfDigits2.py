import sys

file = 'sumofdigits.txt'
fhand = open(file)

#with open(sys.argv[1], 'r') as test_cases:
for test in fhand:
	if len(test) < 1:
		continue
	else:
		sum = 0
		for number in test:
			sum = sum + int(number)
			
			print sum
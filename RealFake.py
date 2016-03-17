#determine which credit cards are real, double every third number starting from the 
#first one, add them together, and then add them to those figures that were not doubled. 
#If the total sum of all numbers is divisible by 10 without remainder, then this credit 
#card is real.

file = 'RealFake.txt'
fhand = open(file, 'r')

for test in fhand:
	s_test = test.strip()
	sum_list = list()
	count = 1
	if s_test == ' ': continue
	else:
		for number in s_test:
			if number == ' ': continue
			else:
				if count == 1 or count == 2:
					sum_list.append(int(number))
					count = count + 1
				else:
					sum_list.append((int(number) * 2))
					count = 1
	if sum(sum_list) % 10 == 0: 
		print 'Real'
	else: 
		print 'Fake'
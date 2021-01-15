def get_x():
	x = input('How many Question Marks do you want?')
	x = int(round(float(x)))

	if x > 0:
		for _ in range(x):
			print('?', end='')
			# end='' newline açmasın diye
	else:
		print('Enter acceptible value')
		get_x()

get_x()

"""
algorithm:
1- ask x.
2- because python inputs default to string, use int(x)
3- is x greater than 0? A)True B)False

4A- use range(x) to make a sequence of number
5A- go throught the range(x) sequence with for _ in
6AT- print "?"

4B- print "Enter an acceptible value"
5B- start get_x() again

# ve farkındayım, boş kod uzatmaya giriyor
"""

# IMPORTS

import random
import time

# MAIN CODE

def in_():
	# get x and y
	x = input('Width: ')
	x = int(x)
	y = input('Length: ')
	y = int(y)

	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			time.sleep(0.45)
	else:
		print('Enter acceptible value')
		# restart process
		in_()

def in_x(min_y=1, max_y=99, y=None):
	# check if int
	if not (type(min_y) == int) & (type(max_y) == int):
		raise TypeError
	
	# calculate y
	if y == None:
		y = random.randint(min_y,max_y)
	else:
		# check if int
		if not (type(y) == int):
			raise TypeError
	
	# get x
	x = input('Width: ')
	x = int(x)
	
	# check if x and y are greater than 0
	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			time.sleep(0.45)
	else:
		print('Enter acceptible value')
		# restart process
		in_x(y=y)

def in_y(min_x=1, max_x=99, x=None):
	# check if int
	if not (type(min_x) == int) & (type(max_x) == int):
		raise TypeError
	
	# calculate y
	if x == None:
		x = random.randint(min_x,max_x)
	else:
		# check if int
		if not (type(x) == int):
			raise TypeError
	
	# get x
	y = input('Length: ')
	y = int(y)
	
	# check if x and y are greater than 0
	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			time.sleep(0.45)
	else:
		print('Enter acceptible value')
		# restart process
		in_y(x=x)

def pre(min_x = 1, min_y = 1, max_x = 99, max_y = 99, x = None, y = None):
	# check if int
	if not (type(min_x) == int) & (type(max_x) == int) & (type(min_y) == int) & (type(max_y) == int):
		raise TypeError
	
	# calcute x
	if x == None:
		x = random.randint(min_x,max_x)
	else:
		# check if int
		if not (type(x) == int):
			raise TypeError
	
	# calcute y
	if y == None:
		y = random.randint(min_y,max_y)
	else:
		# check if int
		if not (type(y) == int):
			raise TypeError
	
	# check if x and y are greater than 0
	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			time.sleep(0.45)
	else:
		print('Enter acceptible value')
		# restart process
		pre(x=x, y=y)

def f_in_():
	# get x and y
	x = input('Width: ')
	x = int(x)
	y = input('Length: ')
	y = int(y)

	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			
	else:
		print('Enter acceptible value')
		# restart process
		f_in_()

def f_in_x(min_y=1, max_y=99, y=None):
	# check if int
	if not (type(min_y) == int) & (type(max_y) == int):
		raise TypeError
	
	# calculate y
	if y == None:
		y = random.randint(min_y,max_y)
	else:
		# check if int
		if not (type(y) == int):
			raise TypeError
	
	# get x
	x = input('Width: ')
	x = int(x)
	
	# check if x and y are greater than 0
	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			
	else:
		print('Enter acceptible value')
		# restart process
		f_in_x(y=y)

def f_in_y(min_x=1, max_x=99, x=None):
	# check if int
	if not (type(min_x) == int) & (type(max_x) == int):
		raise TypeError
	
	# calculate y
	if x == None:
		x = random.randint(min_x,max_x)
	else:
		# check if int
		if not (type(x) == int):
			raise TypeError
	
	# get x
	y = input('Length: ')
	y = int(y)
	
	# check if x and y are greater than 0
	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			
	else:
		print('Enter acceptible value')
		# restart process
		f_in_y(x=x)

def f_pre(min_x = 1, min_y = 1, max_x = 99, max_y = 99, x = None, y = None):
	# check if int
	if not (type(min_x) == int) & (type(max_x) == int) & (type(min_y) == int) & (type(max_y) == int):
		raise TypeError
	
	# calcute x
	if x == None:
		x = random.randint(min_x,max_x)
	else:
		# check if int
		if not (type(x) == int):
			raise TypeError
	
	# calcute y
	if y == None:
		y = random.randint(min_y,max_y)
	else:
		# check if int
		if not (type(y) == int):
			raise TypeError
	
	# check if x and y are greater than 0
	if (x > 0) & (y > 0):
		for _ in range(y):
			for _ in range(x):
				print('#', end='')
			print('')
			
	else:
		print('Enter acceptible value')
		# restart process
		f_pre(x=x, y=y)

f_pre(1,1,10,10)

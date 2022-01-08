# Add implementation
def add(x,y):
	return x+y

# Substract implementation
def substract(x,y):
	return x-y	#on master branch

# Multiply implementation
def multiply(x,y):
	return x*y	#on Bug456

# Divide implementation
def divide(x,y):
	if y==0:
		return DIVIDE_BY_0_ERROR
	else:
		return x/y

# Square implementation	#before stash
def square(x):
	return x^2

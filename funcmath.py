def square(n):
	"""Square a number."""
	return n * n

def power(base, exponent):
	"""Raise base to the power of exponent."""
	return base ** exponent

# Examples
# square
number = float(raw_input("Enter a number: "))
print "Square of %r is: %f." % (number, square(number))

print "%r ** %r is: %f." % (number, number, power(number, number))

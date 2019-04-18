def square(n):
	"""Square a number."""
	return n * n


# Examples
# square
number = float(raw_input("Enter a number: "))
print "Square of %r is: %f." % (number, square(number))

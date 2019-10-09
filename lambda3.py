def multiply(x):
	return lambda y : y * x

double = multiply(2)
triple = multiply(3)
multiply5 = multiply(5)
multiply9 = multiply(9)

print "double(6) = ", double(6)
print "triple(6) = ", triple(6)
print "multiply5(6) = ", multiply5(6)
print "multiply9(6) = ", multiply9(6)


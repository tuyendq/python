def adder(x):
	return lambda y: x + y

add5 = adder(5)
addfive = adder(5)
add9 = adder(9)

print "add5(1) = ", add5(1)
print "addfive(1) = ", add5(1)
print "add9(1) = ", add9(1)

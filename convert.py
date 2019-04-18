def f_to_c(f):
    return (f - 32) * 5 / 9

F = raw_input("Enter temperature in Fahrenheit: ")

print "%r Fahrenheit is %f in Celcius." % (F, f_to_c((float)(F)))

# print f_to_c(F)

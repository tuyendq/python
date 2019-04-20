from sys import argv
import random

script, file_name = argv

# test first
print "arg1: %r, arg2: %r" % (script, file_name)

# Todo: add exception
input_file = open(file_name, 'r')

random_number = random.randint(1, 8)

for i in range(1, random_number):
    input_file.readline()

qotd =  input_file.readline()
print qotd

input_file.close()

from sys import argv
import random
import csv

script, file_name, file_html = argv

# test first
print "arg1: %r, arg2: %r, arg3: %r" % (script, file_name, file_html)

# Todo: add exception
input_file = open(file_name, 'r')

random_number = random.randint(1, 8)

for i in range(1, random_number):
    input_file.readline()

qotd =  input_file.readline()
print qotd

input_file.close()

content = csv.reader(qotd)
print list(content)

output_file = open(file_html, 'w')
output_file.write(qotd)
output_file.close()

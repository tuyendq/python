from sys import argv
import random
import csv

script, file_name, file_html = argv

# test first
print "arg1: %r, arg2: %r, arg3: %r" % (script, file_name, file_html)

# Todo: add exception
with open(file_name, 'r') as input_file:
	contents = csv.reader(input_file)
	print """===Print all==="""
	for row in contents:
		print row[0]
		print row[1]
		print """===""" 

	print """===Print a random quote==="""
	# random_number = random.randint(1, 8)
	print contents

	# qotd = contents[random_number]
	
	# print qotd
	# for i in range(1, random_number):
    #	input_file.readline()

#qotd =  input_file.readline()
#print qotd

#input_file.close()


output_file = open(file_html, 'w')
#output_file.write(qotd)
output_file.close()

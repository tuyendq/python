from sys import argv
script, file_name = argv

# test first
print "arg1: %r, arg2: %r" % (script, file_name)

# Todo: add exception
input_file = open(file_name, 'r')

for i in range(1, 3):
    input_file.readline()

qotd =  input_file.readline()
print qotd

input_file.close()

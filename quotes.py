from sys import argv
import random
import csv

script, file_name, file_html = argv

# test first
# print "arg1: %r, arg2: %r, arg3: %r" % (script, file_name, file_html)

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

	# qotd = contents[random_number]
	
	# print qotd
	# for i in range(1, random_number):
    #	input_file.readline()




def create_html(file_html, quote_content, quote_author):
		html_content = """
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset="utf-8">
		<title>What, Why, and How to practice habit?</title>
		<link rel="stylesheet" href="styles.css">
		</head>

		<body>
		<center>
		<blockquote>{quote_content}</blockquote>
		<author>&mdash; {quote_author}</author>
		</center>
		</bofy>

		</html>

		"""
		html_content = html_content.format(quote_content=quote_content, quote_author=quote_author)

		output_file = open(file_html, 'w')
		output_file.write(html_content)
		output_file.close()


quote_content = "Everything is practice"
quote_author = "Pele"

create_html(file_html, quote_content, quote_author)


#!/usr/bin/env python

# print("Count words frequency in text file")

from collections import Counter
# python v2
# from io import open

# print(Counter(open("tngh.txt","r", encoding="utf-8").read()))
result = Counter(open("tngh.txt","r", encoding="utf-8").read())

outfile = "tngh_freq.csv"
# print(outfile)
with open(outfile, mode="w", encoding="utf-8", newline="") as fp:
    # Write header line
    fp.write("Word,Frequency\n")
    for char, count in result.items():
        fp.write("{},{}\n".format(char,count))


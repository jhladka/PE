#!/usr/bin/python

"""
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.
However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above.
"""

from math import log

F = open('p099_base_exp.txt','r')

w = F.readline().split(',')
base1 = int(w[0])
exp1 = int(w[1])
L = 1
maxline = 1
for line in F :
	w = line.split(',')
	base2 = int(w[0])
	exp2 = int(w[1])
	L += 1
	if exp1*log(base1) < exp2*log(base2) :
		maxline = L
		exp1 = exp2
		base1 = base2
F.close()
print maxline

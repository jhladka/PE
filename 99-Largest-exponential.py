#!/usr/bin/python
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

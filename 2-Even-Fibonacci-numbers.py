#!/usr/bin/python
    
MAX = 4000000

i = 1
j = 2
s = i+j
SUM = 2
while s <= MAX :
#	print i,j,i+j
	if s % 2 == 0 : 
		SUM += s
		#print s
	i = j
	j = s
	s = i+j
	#print s

print SUM

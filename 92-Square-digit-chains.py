#!/usr/bin/python

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,
44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
"""
MAX = pow(10,7)
end1 = set([1])
squares = {}
for i in xrange(10):
	squares[str(i)] = i**2
N = 0
for n in xrange(2,MAX) :
	a = n
	while a <> 89 :
		b = str(a)
		a = sum(squares[c] for c in b)
		if a < n :
			if a not in end1 :
				N += 1
				break
			else : 
				end1.add(n)
				break
	if a >= n and a == 89 : 
		N += 1  
	#if n%10000 == 0 : print n, N
print N

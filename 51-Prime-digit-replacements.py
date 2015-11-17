#!/usr/bin/python

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

def primes_less_than(m):
    P = [2,3,5,7,11,13]
    if m < 17 : return [x for x in P if x < m]
    candidates = [x for x in xrange(17,m,2) if x%3 and x%5 and x%7 and x%11 and x%13]
    candidates.reverse()
    s = m**0.5
    while candidates <> [] :
        i = candidates.pop()
        P.append(i)
        if i <= s : candidates = filter(lambda x : x%i , candidates)
        else : break
    candidates.reverse()
    P.extend(candidates)
    return P

n = 3
while 1 :
	P_set = set(primes_less_than(pow(10,n)))-set(primes_less_than(pow(10,n-1)))
	P_list = list(P_set)
	for A in P_list :
		B = list(str(A))
		dup012 = [[],[],[]] 	# ulozi sem indexy 0,1,2
		for i in range(len(B)) :
			if int(B[i]) < 3 : dup012[int(B[i])].append(i)
		for i in range(len(dup012)) :
			N = 1 	# pocet najdenych prvocisel
			if len(dup012[i]) > 1 :
				for j in range(i+1,10) :
					B_test = list(B)
					for k in dup012[i] : B_test[k] = str(j)
					t = ''.join(B_test)
					test = int(t)
					if test in P_set : N += 1
			if N >= 8 : 
				print A
				quit()
			#if N >= 7 : print N, A
	n += 1
	print 'Prechadzam ',n,'-ciferne prvocisla'

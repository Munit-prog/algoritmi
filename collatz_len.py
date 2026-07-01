def len_pipoz(n):
	m = n
	lunghezza = 1
	while (m!=1):
		if m % 2==0 :
			m=m//2
		else:
			m=3*m+1
		lunghezza+=1
	return lunghezza
print (len_pipoz(3))

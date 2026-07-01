def search (A,key):
	inizio = 0
	fine = len(A)-1
	while (inizio<=fine):
		m = (inizio+fine)//2
		if A[m] == key :
			return m
		elif A[m]<key :
			inizio = m+1
		else:
			fine = m - 1
	return None

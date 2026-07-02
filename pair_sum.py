#caso peggiore O(n^2), sommatoria dei primi n interi

def find_pair(A,key):
	for i in range (0,len(A)):
		for j in range (i+1, len(A)):
			if A[i]+A[j]==key:
				return (i,j)
	return None

#caso medio O(nlogn), non ottimale

def find_pair2(A,key):
	for i in range (0,len(A)):
		val=key-A[i]
		start=i+1
		j=len(A)-1
		while start<=j:
			med=(start+j)//2
			if A[med] == val:
				j = med
				return (i,j)
			elif A[med] < val:
				start=med+1
			else:
				j = med-1
	return None
#caso migliore O(n)

def find_pair3(A,key):
	i=0
	j=len(A) - 1
	while i<j:
		somma = A[i]+A[j]
		if key == somma:
			return (i,j)
		elif key > somma:
			i += 1
		else:
			j -=1
	return None


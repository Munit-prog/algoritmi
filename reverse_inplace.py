def reverse (A) :
	n=len(A)
	for i in range(0, n//2):
		j = n-1-i
		x = A[i]
		A[i] = A[j]
		A[j] = x
	return A

print(reverse ([1,2,3,4,5,6]))

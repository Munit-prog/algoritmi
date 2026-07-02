def first(A, key):  #trova posizione primo key
	start = 0
	end = len(A) - 1
	candidate = -1
	while start <= end:
		med = (start+end)//2
		if A[med] == key:
			candidate = med
			end = med - 1
		elif A[med] < key:
			start=med+1
		else:
			end = med - 1
	return candidate

def last(A,key): #trova posizione ultimo key
	start=0
	end = len(A) - 1
	candidate = -1
	while start <= end:
		med = (start+end)//2
		if A[med] == key:
			candidate = med
			start = med + 1
		elif A[med] < key:
			start = med+1
		else:
			end = med - 1
	return candidate

def count(A,key):
	x = first(A,key)
	y = last(A,key)
	if x < 0:
		return 0
	return y - x +1

print (count([3,7,8,11,15,24],15))
print (count([3,7,7,7,15,15],7))


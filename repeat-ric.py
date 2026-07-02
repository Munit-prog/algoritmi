def first(A, key, start, end):
	if start > end:
		return -1
	med = (start + end) // 2
	if key == A[med]:
		candidate = first(A,key,start,med-1)
		if candidate == -1:
			return med
		else: return candidate
	elif key < A[med]:
		return first(A,key,start,med-1)
	else:
		return first(A,key,med+1,end)

def last(A,key,start,end):
	if start > end:
		return -1
	med = (start + end) // 2
	if key == A[med]:
		candidate = last(A,key,med+1,end)
		if candidate == -1:
			return med
		else: return candidate
	elif  key < A[med]:
		return last(A,key,start,med-1)
	else:
		return last(A,key,med+1,end)

def count(A,key):
	start=0
	end=len(A)-1
	primo = first(A,key,start,end)
	ultimo = last(A,key,start,end)
	if primo < 0:
		return 0
	else :
		return ultimo - primo + 1 

print (count([3,7,8,11,15,24],15))
print (count([3,7,7,7,15,15],7))




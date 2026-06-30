def reverse(i):
	risultato = []
	for y in range (len(i)-1,0-1,-1):
		invertito= i[y]
		risultato.append(invertito)
	return risultato

print(reverse([1,2,3,4,5,6,7]))

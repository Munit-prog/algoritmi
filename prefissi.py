def prefix(s):
	risultato=[]
	for i in range(len(s),0-1,-1):  #0-1 perchè senno range esclude lo 0
		prefisso=s[:i]
		risultato.append(prefisso)
	return risultato

#riordinati dalla stringa più lunga a quella più corta

print(prefix("Hello"))

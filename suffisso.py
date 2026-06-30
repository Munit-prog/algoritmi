def suffixes(s):
    risultato=[]
    for i in range(0,len(s)+1):
        suffisso=s[i:]
        risultato.append(suffisso)
    return risultato

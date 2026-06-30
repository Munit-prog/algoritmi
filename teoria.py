#variabili e tipi fondamentali
x = 5          # int (interi a precisione arbitraria, niente overflow)
y = 3.14       # float
flag = True    # bool (True / False, con la maiuscola)
nome = "Saro"  # str
nulla = None   # il valore "niente", analogo a NIL in CLRS

#int, float, bool, str, tuple sono immutabili; list, dict, set sono mutabili

#operatori
7 / 2     # 3.5   divisione "vera", restituisce sempre float
7 // 2    # 3     divisione INTERA (floor) — questa è quella di CLRS
7 % 2     # 1     modulo (es. hashing per concatenamento)
2 ** 10   # 1024  potenza

a == b      # uguaglianza (== non =)
a != b      # diverso
a < b <= c  # confronti concatenati, leciti e leggibili
not, and, or  # operatori logici scritti a parole, non !, &&, ||

#strutture di controllo e identazione
#condizionale
if x > 0:
    segno = 1
elif x < 0:
    segno = -1
else:
    segno = 0

#il ciclio while
i = 0
while i < n:
    # corpo
    i = i + 1   # oppure i += 1

#for itera su sequenza. Per contatore numerico si usa range
range(n)         # 0, 1, ..., n-1
range(a, b)      # a, a+1, ..., b-1   (estremo destro escluso)
range(a, b, s)   # con passo s; range(n-1, -1, -1) per andare a ritroso

for i in range(n):     # equivale a "for i = 0 to n-1"
    print(i)
#range (1,n) produce 1,...,n-1. Con for estremo va aggiustato

#strutture dati incorporate
#lista - array dinamico
A = [5, 2, 9, 1]
A[0]        # 5    indicizzazione da 0
A[-1]       # 1    indice negativo: ultimo elemento
A[i] = 99   # assegnazione in posizione (in-place)
len(A)      # 4    lunghezza, è A.length di CLRS
A.append(7) # aggiunge in coda (ammortizzato O(1))

#lo slicing estrae sottoquenze (crea una copia)
A[1:3]    # elementi dagli indici 1 e 2 → [2, 9]
A[:k]     # primi k elementi
A[k:]     # dal k-esimo in poi

#per le matrici si usano liste di liste
M = [[0]*n for _ in range(n)]   # matrice n×n di zeri
M[i][j] = 1

#dizionario (dict) - tabella di hash
D = {}              # dizionario vuoto
D["chiave"] = 42    # inserimento
D["chiave"]         # accesso
"chiave" in D       # test di appartenenza, O(1) atteso
del D["chiave"]     # cancellazione
D.get(k, default)   # accesso senza errore se la chiave manca

#insieme (set) - insieme non ordinato, utile per i vertici visitati
visitati = set()
visitati.add(v)
if u not in visitati: ...

#tupla (tuple) - sequenza immutabile, utile per coppie o per restituire valori
arco = (u, v)

#funzioni, si definiscono con def, e return restituisce un valore
def somma(a, b):
    return a + b

#valori di default e restituire più valori tramite tupla
def dividi(a, b=2):
    return a // b, a % b      # restituisce una tupla

q, r = dividi(17, 5)          # spacchettamento: q=3, r=2

#se passi una lista a una funzione e la modifichi in posizione, la modifica è
#visibile fuori
def incrementa_primo(A):
    A[0] += 1      # modifica l'originale

L = [10, 20]
incrementa_primo(L)
# L è ora [11, 20]

#ricorsione
def fattoriale(n):
    if n <= 1:        # caso base
        return 1
    return n * fattoriale(n - 1)

#costrutti idiomatici
#lo scambio senza variabile temporanea
A[i], A[j] = A[j], A[i]      # scambia i due elementi

#valore "infinito" 
INF = float('inf')
d = [float('inf')] * n

#enumerate per iterare con indice e valore insieme
for i, valore in enumerate(A):
    ...

#list comprehension per costruire liste in modo conciso
quadrati = [x*x for x in range(n)]
pari = [x for x in A if x % 2 == 0]

#moduli libreria standard
#import carica un modulo

import heapq         # coda di priorità (min-heap) — per Dijkstra/Prim
import math          # math.inf, math.floor, math.log, ...
from collections import deque   # coda doppia O(1) agli estremi, per BFS
#heapq ti dà un min-heap pronto: heapq.heappush(h,x) e heapq.heappop(h).



def insertion_sort(A):
    # ordina A in posizione (in-place)
    for j in range(1, len(A)):
        chiave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chiave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chiave


if __name__ == "__main__":
    print("Ambiente Python funzionante ✓")

    A = [5, 2, 4, 6, 1, 3]
    print("Prima: ", A)
    insertion_sort(A)
    print("Dopo:  ", A)

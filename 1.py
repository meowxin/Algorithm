#Insertion Sort
def InsertionSort(A):
    """Insertion sort"""
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i -1 
        A[i+1] = key

#Merge Sort
def merge(A, p, q, r):
    L = A[p : q]
    R = A[q : r]
    i, j = 0, 0
    for k in range(p, r):
        if len(L)==i:
            for rms in range(j,len(R)):
                A[k] = R[rms]
                k += 1
            return
        elif len(R)==j:
            for rms in range(i,len(L)):
                A[k] = L[rms]
                k += 1
            return
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, p, r):
    if (r - p) > 1 :
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q, r)
        merge(A, p, q, r)


#Test Functions

import random
data = random.sample(range(10),6)

print("Before Insertion Sort: \n", data)
InsertionSort(data)
print("After: \n", data)

data = random.sample(range(10),6)
print("Before Merge Sort: \n", data)
mergeSort(data, 0, len(data))
print("After: \n", data)
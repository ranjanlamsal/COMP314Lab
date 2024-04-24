#selection_sort.py
def selection_sort(A):
    n = len(A)
    
    for  i in range(n-1):
        m = i
        for j in range(i+1, n):
            if A[j] < A[m]:
                m = j
        temp = A[i]
        A[i] = A[m]
        A[m] = temp
    
    return A

if __name__ == '__main__':
    B = [1, 0, 9, 100, 30, 45,2]

    print(selection_sort(B))

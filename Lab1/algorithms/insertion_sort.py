#insertion_sort.py
def insertion_sort(A):
    n = len(A)
    for  i in range(1, n):
        value = A[i]
        j = i-1
        
        while(j >=0 and value < A[j]):
            A[j+1] = A[j]
            j = j-1
        
        A[j+1] = value
        
    
    return A

if __name__ == '__main__':
        
    A = [1,5,2,3,7,9,0,2]

    print(insertion_sort(A))

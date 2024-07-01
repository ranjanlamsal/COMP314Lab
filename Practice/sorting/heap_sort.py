def Heapify_max(A,N,i):
    l = 2*i + 1
    r = 2*i + 2
    
    if l < N and A[l] > A[i]:
        largest = l
    
    else:
        largest = i
        
    if r < N and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        
        Heapify_max(A,N,largest)
    
        

def Build_Max_Heap(A):
    N = len(A)
    for i in range(N//2 -1, -1 , -1):
        Heapify_max(A,N, i)
        

def Heap_sort(A):
    
    Build_Max_Heap(A)
    
    N = len(A)

    for i in range(N-1,0,-1):
        A[i], A[0] = A[0], A[i]
        Heapify_max(A, i,0)
        
def main():
    A = [5, 3, 4, 1, 2,18, 10,1,2,3,4,5, 9, 7, 2, 0, 1, 5]
    
    print(f"Original Array: {A}")
    
    Heap_sort(A)
    
    print(f"Sorted Array:   {A}")
    
    
if __name__ == "__main__":
    main()
import math

def merge_sort(arr, p, r):
    if p < r :
        q = (p+r)//2
        
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        
        return merge(arr, p, q, r)
    

def merge(arr, p, q, r):
    print(f'p: {p}, q: {q}')
    n1 = q-p+1
    n2 = r-q
    
    print(f'n1: {n1}, n2: {n2}')
    
    
    L= [0]*(n1+1)
    R= [0]*(n2+1)
    
    for i in range(n1):
        L[i] = arr[i+p]
        
    for j in range(n2):
        R[j] = arr[j+q+1]
        
    L[n1] = math.inf
    R[n2] = math.inf
    
    print(f'L: {L}, R: {R}')
    print(f'arr: {arr}')
    
    i = 0
    j = 0
    
    for k in range(p, r+1):
        if L[i]<=R[j]:
            arr[k] = L[i]
            i = i+1
        
        else:
            arr[k] = R[j]
            j = j+1
    
    return arr

def main():
    arr =[2,4,45,1,2,0,9,4,32,2,5,6,8,32,1,6,0,1]
    
    print(f"original array: {arr}")
    sorted_array = merge_sort(arr, 0, len(arr)-1)
    
    print(f"sorted array: {sorted_array}")
    
if __name__ == "__main__":
    main()
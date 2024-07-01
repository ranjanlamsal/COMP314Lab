def sequential(arr, key):
    i = 0
    
    while i<len(arr) and arr[i] != key:
        i+=1
    
    if i<len(arr):
        return i
    
    return -1

if __name__ == "__main__":
    
    arr= [100, 3, 1, 6, 77, 0, 1, 3,4, 1 , 2, 0, 9, 88, 0]
    print(f"Original: {arr}")
    
    key = sequential(arr, 4)
    
    print(f"Search key: {key}")
    
def bubble(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

if __name__ == "__main__":
    
    arr= [100, 3, 1, 6, 77, 0, 1, 3,4, 1 , 2, 0, 9, 88, 0]
    print(f"Original: {arr}")
    sorted_array = bubble(arr)
    
    print(f"Sorted: {sorted_array}")
    
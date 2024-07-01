def insertion_sort(arr):
    n = len(arr)
    
    for j in range(1, n):
        key = arr[j]
        i = j-1
        
        while i >=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i-1
        
        arr[i+1] = key
    
    return arr

def main():
    arr = [5, 3, 4, 1, 2,18, 10,1,2,3,4,5, 9, 7, 2, 0, 1, 5]
    
    print(f"Original Array: {arr}")
    sorted_arr = insertion_sort(arr)
    
    print(f"Sorted Array:   {sorted_arr}")
    
if __name__ == "__main__":
    main()
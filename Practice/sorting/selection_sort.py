"""
Steps:
iterate i from 0 to n-1:
    iterate j from i+1 to n:
        if a[i]>a[j]
        swap a[i] & a[j]
    Select the smallest element from the unsorted sublist and exchange it with the element at the begining of the unsorted data.
Repeat
"""

def selection_sort(arr):
    n = len(arr)
    
    for i in range (0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def main():
    arr = [5, 3, 4, 1, 2,18, 10,1,2,3,4,5, 9, 7, 2, 0, 1, 5]
    
    print(f"Original Array: {arr}")
    sorted_arr = selection_sort(arr)
    
    print(f"Sorted Array:   {sorted_arr}")
    
if __name__ == "__main__":
    main()
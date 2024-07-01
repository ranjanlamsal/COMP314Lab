def quick_sort(arr, p, r):
    if p<r:
        q = partition(arr, p, r)
        quick_sort(arr, p,q-1)
        quick_sort(arr, q+1, r)
        
        return arr
        

def partition(arr, p, r):
    # make pivot element at index r
    
    pivot = arr[r]
    # we need to indices, one for every element and one to maintain the index of pivot at the end of partition
    
    i = p-1
    
    for j in range(p, r):
        if arr[j] <= pivot:
            i = i+1
            # for anyelement smaller than pivot shift the i index and then exchange the jth element(that is smaller than pivot)with ith element
            # the idea is that we put any new element that is smaller than pivot at the end of the index of element smaller.
            arr[i], arr[j] = arr[j], arr[i]
            
    # after all the element from p to i are smaller than pivot and all the element from i+1 to r-1 are larger than pivot
    # exchange i+1 element with pivot element
    
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1
            
def main():
    arr = [5, 3, 4, 1, 2,18, 10,1,2,3,4,5, 9, 7, 2, 0, 1, 5]

    print(f"Original Array: {arr}")
    sorted_arr = quick_sort(arr, 0, len(arr)-1)

    print(f"Sorted Array:   {sorted_arr}")

if __name__ == "__main__":
    main()
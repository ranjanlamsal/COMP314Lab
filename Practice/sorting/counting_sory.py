# calculate frequencies of each input integer and then sort based om this frequency


def counting_sort(arr):
    
    M = max(arr)
    
    count_array = [0]*(M+1)
    
    #Calculate frequency of each elements
    for num in arr:
        count_array[num] += 1
    
    #calculate cumulative frequency
    for i in range(1, M+1):
        count_array[i] += count_array[i-1]
    
    output = [0]*len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        output[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -=1
        
    return output

if __name__ == "__main__":
    # Input array
    input_array = [4, 3, 12, 1, 5, 5, 3, 9]
 
    # Output array
    output_array = counting_sort(input_array)
 
    for num in output_array:
        print(num, end=" ")
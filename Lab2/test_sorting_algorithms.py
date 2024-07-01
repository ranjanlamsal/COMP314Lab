
from merge import merge_sort
from quick_sort import quick_sort
from generate_array import generate_array

random_array = generate_array(1000)
sorted_random_arry = sorted(random_array)
def test_sorting_algorithms():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
        ([0, -1, 5, -3, 8, -2], [-3, -2, -1, 0, 5, 8]),
        (random_array, sorted_random_arry)
    ]
    
    for i, (input_arr, expected) in enumerate(test_cases):
        arr_copy_merge = input_arr.copy()
        arr_copy_quick = input_arr.copy()
        
        merge_sort(arr_copy_merge, 0, len(arr_copy_merge) - 1)
        quick_sort(arr_copy_quick, 0, len(arr_copy_quick) - 1)
        
        assert arr_copy_merge == expected, f"Merge Sort Test Case {i+1} Failed"
        assert arr_copy_quick == expected, f"Quick Sort Test Case {i+1} Failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_sorting_algorithms()

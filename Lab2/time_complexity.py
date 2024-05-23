#time_complexity.py

from merge import merge_sort
from quick_sort import quick_sort
from generate_array import generate_array
from time import time


def calculate_merge_time(n):
    testArray1 = generate_array(n)

    start = time()

    resultArray1_insertion = merge_sort(testArray1, 0, len(testArray1)-1)

    end = time()

    return end - start
    
    
def calculate_quick_time(n):
    testArray1 = generate_array(n)

    start = time()

    resultArray1_selection = quick_sort(testArray1, 0, len(testArray1)-1)

    end = time()

    return end - start
    

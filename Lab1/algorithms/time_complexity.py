#time_complexity.py

from insertion_sort import insertion_sort
from selection_sort import selection_sort
from generate_array import generate_array
from time import time


def calculate_insertion_time(n):
    testArray1 = generate_array(n)

    start = time()

    resultArray1_insertion = insertion_sort(testArray1)

    end = time()

    return end - start
    
    
def calculate_selection_time(n):
    testArray1 = generate_array(n)

    start = time()

    resultArray1_selection = selection_sort(testArray1)

    end = time()

    return end - start
    

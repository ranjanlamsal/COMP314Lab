import unittest
from insertion_sort import * 
from selection_sort import *
from merge_sort import *
from quick import *

original_array = [2,4,45,1,2,0,9,4,32,2,5,6,8,32,1,6,0,1]
sorted_array = [0, 1, 1, 3, 2, 3, 4, 2, 5, 4, 5, 2, 5, 7, 9, 10, 18, 1]


class test_sorting_algorithms(unittest.TestCase):
    
    # def test_selection(self):
    #     output = selection_sort(original_array)
    #     self.assertEqual(output, sorted_array)
        
    # def test_insertion(self):
    #     output = insertion_sort(original_array)
    #     self.assertEqual(output, sorted_array)
        
    # def test_merge(self):
    #     output = merge_sort(original_array, 0 , len(original_array)-1)
    #     self.assertEqual(output, sorted_array)
    
    def test_quick(self):
        output = quick_sort(original_array, 0, len(original_array)-1)
        self.assertEqual(output, sorted_array)
        

if __name__ == "__main__":
    unittest.main()
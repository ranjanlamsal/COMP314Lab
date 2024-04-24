#test_sorting.py
import unittest
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort

class TestSort(unittest.TestCase):    
    def test_insertion_sort(self):
        input_data = [3,4,2]
        result = insertion_sort(input_data)
        
        self.assertEqual(result, [2,3,4])
    
    def test_selection_sort(self):
        input_data = [2,4,1,9,6]
        result = selection_sort(input_data)
        self.assertEqual(result, [1,2,4,6,9])



if __name__ == '__main__':
    unittest.main()
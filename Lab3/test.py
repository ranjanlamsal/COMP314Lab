import unittest
from knapsack import *

class TestKnapsackAlgorithms(unittest.TestCase):

    # Simple implementation
    def test_fractional_bruteforce_simple(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 40
        expected_value = 200.0
        expected_combination = [(60, 10), (100, 20), (40.0, 10)]
        value, combination = fractional_knapsack_brute_force(items, capacity)
        self.assertAlmostEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_bruteforce_simple(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 40
        expected_value = 180
        expected_combination = ((60, 10), (120, 30))
        value, combination = knapsack_0_1_brute_force(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)
        
    def test_fractional_knapsack_greedy_simple(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 40
        expected_value = 200.0
        expected_combination = [(60, 10), (100, 20), (40.0, 10.0)] 
        value, combination = fractional_knapsack_greedy(items, capacity)
        self.assertAlmostEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_knapsack_dp_simple(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 50
        expected_value = 220
        expected_combination = [(120, 30), (100, 20)]
        value, combination = knapsack_0_1_dp(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)
        
    # No items
    def test_fractional_bruteforce_no_items(self):
        items = []
        capacity = 50
        expected_value = 0
        expected_combination = []
        value, combination = fractional_knapsack_brute_force(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_bruteforce_no_items(self):
        items = []
        capacity = 50
        expected_value = 0
        expected_combination = []
        value, combination = knapsack_0_1_brute_force(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)
        
    def test_fractional_greedy_no_items(self):
        items = []
        capacity = 50
        expected_value = 0
        expected_combination = []
        value, combination = fractional_knapsack_greedy(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_dp_no_items(self):
        items = []
        capacity = 50
        expected_value = 0
        expected_combination = []
        value, combination = knapsack_0_1_dp(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)
        
    # Zero Capacity
    def test_fractional_knapsack_zero_capacity(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 0
        expected_value = 0
        expected_combination = []
        value, combination = fractional_knapsack_brute_force(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_knapsack_zero_capacity(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 0
        expected_value = 0
        expected_combination = []
        value, combination = knapsack_0_1_brute_force(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    # Large capacity and items
    def test_fractional_knapsack_large(self):
        items = [(60, 10), (100, 20), (120, 30), (150, 40), (200, 50)]
        capacity = 100
        expected_value = 440.0
        expected_combination = [(60, 10), (100, 20), (200, 50), (80.0, 20)]
        value, combination = fractional_knapsack_brute_force(items, capacity)
        self.assertAlmostEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_knapsack_large(self):
        items = [(60, 10), (100, 20), (120, 30), (150, 40), (200, 50)]
        capacity = 100
        expected_value = 430
        expected_combination = ((60, 10), (100, 20), (120, 30), (150, 40))
        value, combination = knapsack_0_1_brute_force(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_fractional_knapsack_greedy_large(self):
        items = [(60, 10), (100, 20), (120, 30), (150, 40), (200, 50)]
        capacity = 100
        expected_value = 440.0
        expected_combination = [(60, 10), (100, 20), (120, 30), (160.0, 40.0)]
        value, combination = fractional_knapsack_greedy(items, capacity)
        self.assertAlmostEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

    def test_01_knapsack_dp_large(self):
        items = [(60, 10), (100, 20), (120, 30), (150, 40), (200, 50)]
        capacity = 100
        expected_value = 430
        expected_combination = [(150, 40), (120, 30), (100, 20), (60, 10)]
        value, combination = knapsack_0_1_dp(items, capacity)
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)

if __name__ == "__main__":
    unittest.main()

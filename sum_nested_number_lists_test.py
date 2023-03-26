import unittest
from sum_nested_number_lists import sum_nested_number_lists

class SumNestedListsTest(unittest.TestCase):
    def test_sum_two_level_list(self):
        sut_1 = sum_nested_number_lists([[1, 2], [0], [1, 2 , 3]])
        self.assertEqual(
            sut_1, 9, "should return 9 if a list is equal to: [[1, 2], [0], [1, 2 , 3]]")
        sut_2 = sum_nested_number_lists([[2], [1, 2], [6, 7, 8]])
        self.assertEqual(
            sut_2, 26, "should return 26 if a list is equal to: [[2], [1, 2], [6, 7, 8]]")
        sut_3 = sum_nested_number_lists([[], [1, 5], [8]])
        self.assertEqual(
            sut_3, 14, "should return 14 if a list is equal to: [[], [1, 5], [8]]")

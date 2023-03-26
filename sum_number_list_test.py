import unittest
from sum_number_list import sum_number_list

class SumNestedListsTest(unittest.TestCase):
    def test_empty_list(self):
        sut = sum_number_list([])
        self.assertEqual(sut, 0, "should return 0 if list is empty")

    def test_sum_non_empty_lists(self):
        sut_1 = sum_number_list([2, 4])
        self.assertEqual(sut_1, 6, "should return 6 if a list contains 2 and 4")
        sut_2 = sum_number_list([3, 4, -7])
        self.assertEqual(sut_2, 0, "should return 6 if a list contains 3, 4, -7")

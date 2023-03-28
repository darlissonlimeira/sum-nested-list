import unittest
from sum_nested_number_lists import sum_nested_number_lists, sum_number_list

class SumNestedNumberListsTest(unittest.TestCase):
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


class SumNumberListTest(unittest.TestCase):
    def test_empty_list(self):
        sut = sum_number_list([])
        self.assertEqual(sut, 0, "should return 0 if list is empty")

    def test_sum_non_empty_lists(self):
        sut_1 = sum_number_list([2, 4])
        self.assertEqual(sut_1, 6, "should return 6 if a list contains 2 and 4")
        sut_2 = sum_number_list([3, 4, -7])
        self.assertEqual(sut_2, 0, "should return 6 if a list contains 3, 4, -7")

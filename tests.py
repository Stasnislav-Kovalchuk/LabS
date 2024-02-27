import unittest
from Algolab1 import gardener_bot


class Test(unittest.TestCase):
    def test_five_five(self):
        array = [[2, 4, 5, 6, 7],
                 [8, 9, 10, 11, 12],
                 [13, 14, 15, 16, 17],
                 [18, 19, 20, 21, 22]]

        expected_result = [2, 4, 5, 6, 7, 12, 11, 10, 9, 8, 13, 14, 15, 16, 17, 22, 21, 20, 19, 18]

        self.assertEqual(gardener_bot(array), expected_result)

    def test_two_four(self):
        array = [[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]

        expected_result = [1, 2, 4, 3, 5, 6, 8, 7]

        self.assertEqual(gardener_bot(array), expected_result)

    def test_one_six(self):
        array = [[1],
                 [2],
                 [3],
                 [4],
                 [5],
                 [6]]

        expected_result = [1, 2, 3, 4, 5, 6]

        self.assertEqual(gardener_bot(array), expected_result)

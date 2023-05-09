import sys
sys.path.append("..")

import unittest
from ex00.give_bmi import give_bmi, apply_limit
import numpy as np


class TestBMIFunctions(unittest.TestCase):

    def test_give_bmi_with_int_correct(self):
        self.assertEqual(give_bmi([2, 1], [165, 38]), [41.25, 38])

    def test_give_bmi_with_int_zero_division(self):
        self.assertEqual(give_bmi([0], [165]), [np.inf])

    def test_give_bmi_with_float_zero_division(self):
        self.assertEqual(give_bmi([0.0], [165.0]), [np.inf])

    def test_give_bmi_with_float_correct(self):
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        expected_output = [22.507863455018317, 29.0359168241966]
        self.assertEqual(give_bmi(height, weight), expected_output)

    def test_give_bmi_return_type_correct(self):
        self.assertEqual(type(give_bmi([], [])), list)

    def test_give_bmi_value_error(self):
        with self.assertRaises(SystemExit) as ms:
            give_bmi([2, 1, 1], [3, 4])
        self.assertEqual(ms.exception.code, 1)

    def test_give_bmi_type_error(self):
        with self.assertRaises(SystemExit) as ms:
            give_bmi(["1"], [2])
        self.assertEqual(ms.exception.code, 2)

    def test_apply_limit_with_int_correct(self):
        self.assertEqual(apply_limit([2, 1], 1), [True, False])

    def test_apply_limit_with_float_correct(self):
        self.assertEqual(apply_limit([2.0, 1.0], 1.0), [True, False])

    def test_apply_limit_type_error(self):
        with self.assertRaises(SystemExit) as ms:
            apply_limit(["1"], 2)
        self.assertEqual(ms.exception.code, 5)

    def test_applt_limit_empty_list(self):
        self.assertEqual(apply_limit([], 2), [])


if __name__ == "__main__":
    unittest.main()

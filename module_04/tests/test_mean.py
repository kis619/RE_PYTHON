from unittest import main, TestCase
from ex00.statistics import get_mean, get_median, get_quartile_25_75


class TestMean(TestCase):

    def test_get_mean_happy_case(self):
        self.assertEqual(get_mean((1, 2, 3)), 2)

    def test_get_mean_list_with_one_element(self):
        self.assertEqual(get_mean((1,)), 1)

    def test_get_mean_list_with_one_element_zero(self):
        self.assertEqual(get_mean((0,)), 0)

    def test_get_mean_empty_list(self):
        self.assertEqual(get_mean(()), 0)

    def test_get_mean_not_list(self):
        self.assertRaises(TypeError, get_mean, 1)


class TestMedian(TestCase):

    def test_get_median_happy_case_odd_number_of_elements(self):
        self.assertEqual(get_median((1, 2, 3)), 2)

    def test_get_median_happy_case_even_number_of_elements(self):
        self.assertEqual(get_median((1, 2, 3, 4)), 2.5)

    def test_get_median_list_with_one_element(self):
        self.assertEqual(get_median((1,)), 1)

    def test_get_median_list_with_one_element_zero(self):
        self.assertEqual(get_median((0,)), 0)

    def test_get_median_empty_list(self):
        self.assertEqual(get_median(()), 0)


class TestQuartile(TestCase):
    def test_get_quartile_25_75_happy_case_odd_number_of_elements(self):
        self.assertEqual(get_quartile_25_75((1, 2, 3)), [1.5, 2.5])

    def test_get_quartile_25_75_odd_number_of_elements_odd_quarter(self):
        self.assertEqual(get_quartile_25_75((1, 2, 3, 4, 5)), [2, 4])

    def test_get_quartile_25_75_odd_number_of_elements_even_quarter(self):
        self.assertEqual(get_quartile_25_75((1, 2, 3, 4, 5, 6, 7)), [2.5, 5.5])


if __name__ == "__main__":
    main()

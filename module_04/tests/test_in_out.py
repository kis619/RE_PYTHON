from unittest import TestCase, main
from ex01.in_out import outer, square, pow


class TestPow(TestCase):

    def test_pow_happy_case(self):
        self.assertEqual(pow(3), 27)

    def test_pow_negative(self):
        self.assertEqual(pow(-3), -0.037037037037037035)

    def test_pow_zero(self):
        self.assertEqual(pow(0), 1)

    def test_pow_float(self):
        self.assertEqual(pow(2.5), 9.882117688026186)

    def test_pow_string(self):
        with self.assertRaises(TypeError) as error:
            pow("2")
        self.assertEqual(str(error.exception), "x must be numeric")


class TestSquare(TestCase):

    def test_square_happy_case(self):
        self.assertEqual(square(3), 9)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_square_float(self):
        self.assertEqual(square(2.5), 6.25)

    def test_square_string(self):
        with self.assertRaises(TypeError) as error:
            square("2")
        self.assertEqual(str(error.exception), "x must be numeric")


class TestOuter(TestCase):

    def test_outer_happy_case(self):
        my_counter = outer(3, square)
        self.assertEqual(my_counter(), 9)
        self.assertEqual(my_counter(), 81)
        self.assertEqual(my_counter(), 6561)

    def test_outer_first_arg_string(self):
        with self.assertRaises(TypeError) as error:
            outer("3", square)
        self.assertEqual(str(error.exception), "x must be numeric")

    def test_outer_second_arg_not_function_str(self):
        with self.assertRaises(TypeError) as error:
            outer(3, "7")
        self.assertEqual(str(error.exception), "function must be a function")

    def test_outer_second_arg_not_function_int_constr(self):
        with self.assertRaises(TypeError) as error:
            outer(3, int)
        self.assertEqual(str(error.exception), "function must be a function")


if __name__ == "__main__":
    main()

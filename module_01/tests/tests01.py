import sys
sys.path.append("..")

from ex01.array2D import slice_me
from unittest import TestCase, main


class TestSliceMeErrors(TestCase):

    def test_slice_me_1st_arg_not_a_list_type_error(self):
        with self.assertRaises(TypeError):
            slice_me({"1"}, 2, 3)

    def test_slice_me_2nd_arg_not_an_int_type_error(self):
        with self.assertRaises(TypeError):
            slice_me([1], "2", 3)

    def test_slice_me_3rd_arg_not_an_int_type_error(self):
        with self.assertRaises(TypeError):
            slice_me([1], 2, "3")
    
    def test_slice_me_list_elements_different_size(self):
        with self.assertRaises(ValueError):
            slice_me([[1], [2, 2]], 0, 1)
    

class TestSliceMe(TestCase):
    def test_slice_me_empty_list(self):
        self.assertEqual(slice_me([], 0, 1), [])
    
    def test_slice_me_overlapping_idxs(self):
        self.assertEqual(slice_me([1, 2, 3], 7, 1), [])
    
    def test_slice_me_one_dimensional_array(self):
        self.assertEqual(slice_me([1, 2, 3], 0, 1), [1])


if __name__ == "__main__":
    main()

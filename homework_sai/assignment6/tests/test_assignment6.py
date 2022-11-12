import unittest
import os
import assignment6
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment6(unittest.TestCase):
    def setUp(self):
        self.assignment6 = assignment6

    @weight(3)
    @visibility('visible')
    @number("1.1")
    def test_IteratorClass_1(self):
        self.assertRaises(ValueError, assignment6.IteratorClass,
                          range(5, 10), [1, 2, 3], 'div')

    @weight(3)
    @visibility('visible')
    @number("1.2")
    def test_IteratorClass_2(self):
        self.assertRaises(ValueError, assignment6.IteratorClass, [
                          1, 2, 3], range(5, 10), 'div')

    @weight(3)
    @visibility('visible')
    @number("1.3")
    def test_IteratorClass_3(self):
        self.assertRaises(ValueError, assignment6.IteratorClass, [
                          1, 2, 3], [1, 2, 3], 'abc')

    @weight(3)
    @visibility('visible')
    @number("1.4")
    def test_IteratorClass_4(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        add_iterator = assignment6.IteratorClass(x, y, 'add')
        self.assertEqual([ele for ele in add_iterator], [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("1.5")
    def test_IteratorClass_5(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        sub_iterator = assignment6.IteratorClass(x, y, 'sub')
        self.assertEqual([ele for ele in sub_iterator],
                         [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("1.6")
    def test_IteratorClass_6(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        mul_iterator = assignment6.IteratorClass(x, y, 'mul')
        self.assertEqual([ele for ele in mul_iterator],
                         [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("1.7")
    def test_IteratorClass_7(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        div_iterator = assignment6.IteratorClass(x, y, 'div')
        self.assertEqual([ele for ele in div_iterator],
                         [0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_ListV2_1(self):
        self.assertRaises(ValueError, assignment6.ListV2,  3)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_ListV2_2(self):
        self.assertRaises(ValueError, assignment6.ListV2,  '3')

    @weight(3)
    @visibility('visible')
    @number("2.3")
    def test_ListV2_3(self):
        self.assertRaises(ValueError, assignment6.ListV2,  3.14)

    @weight(3)
    @visibility('visible')
    @number("2.4")
    def test_ListV2_4(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = assignment6.ListV2(list(range(50, 55)))
        result = l1 + l2
        self.assertEqual(type(result),  assignment6.ListV2)

    @weight(3)
    @visibility('visible')
    @number("2.5")
    def test_ListV2_5(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = assignment6.ListV2(list(range(50, 55)))
        result = l1 + l2
        self.assertEqual([ele for ele in result],  [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("2.6")
    def test_ListV2_6(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = assignment6.ListV2(list(range(50, 55)))
        result = l1 - l2
        self.assertEqual([ele for ele in result],  [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("2.7")
    def test_ListV2_7(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = assignment6.ListV2(list(range(50, 55)))
        result = l1 * l2
        self.assertEqual([ele for ele in result],  [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("2.8")
    def test_ListV2_8(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = assignment6.ListV2(list(range(50, 55)))
        result = l1 / l2
        self.assertEqual([ele for ele in result],  [
                         0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.9")
    def test_ListV2_9(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        result = l1 + 5
        self.assertEqual([ele for ele in result],  [10, 11, 12, 13, 14])

    @weight(3)
    @visibility('visible')
    @number("2.10")
    def test_ListV2_10(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        result = l1 - 5
        self.assertEqual([ele for ele in result],  [0, 1, 2, 3, 4])

    @weight(3)
    @visibility('visible')
    @number("2.11")
    def test_ListV2_11(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        result = l1 * 5
        self.assertEqual([ele for ele in result],  [25, 30, 35, 40, 45])

    @weight(3)
    @visibility('visible')
    @number("2.12")
    def test_ListV2_12(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        result = l1 / 5
        self.assertEqual([ele for ele in result],  [1.0, 1.2, 1.4, 1.6, 1.8])

    @weight(3)
    @visibility('visible')
    @number("2.13")
    def test_ListV2_13(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = list(range(50, 55))
        result = l1 + l2
        self.assertEqual([ele for ele in result],  [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("2.14")
    def test_ListV2_14(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = list(range(50, 55))
        result = l1 - l2
        self.assertEqual([ele for ele in result],  [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("2.15")
    def test_ListV2_15(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = tuple(range(50, 55))
        result = l1 * l2
        self.assertEqual([ele for ele in result],  [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("2.16")
    def test_ListV2_16(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        l2 = tuple(range(50, 55))
        result = l1 / l2
        self.assertEqual([ele for ele in result],  [0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.17")
    def test_ListV2_17(self):
        l1 = assignment6.ListV2(list(range(5, 10)))
        self.assertEqual(l1.__repr__(),  '[5, 6, 7, 8, 9]')


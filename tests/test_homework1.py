import unittest

import homework1
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestHomework1(unittest.TestCase):
    def setUp(self):
        self.homework1 = homework1

    @weight(2)
    @visibility('visible')
    @number("1")
    def test_ex1(self):
        value = self.homework1.ex1()
        self.assertEqual(True, value)

    @weight(2)
    @visibility('visible')
    @number("2")
    def test_ex2(self):
        value = self.homework1.ex2()
        self.assertEqual(False, value)

    @weight(2)
    @visibility('visible')
    @number("3")
    def test_ex3(self):
        value = self.homework1.ex3()
        self.assertEqual(10, value)

    @weight(2)
    @visibility('visible')
    @number("4")
    def test_ex4(self):
        value = self.homework1.ex4()
        self.assertEqual(3.5, value)

    @weight(2)
    @visibility('visible')
    @number("5")
    def test_ex5(self):
        value = self.homework1.ex5()
        self.assertEqual('a', value)

    @weight(2)
    @visibility('visible')
    @number("6")
    def test_ex6(self):
        value = self.homework1.ex6()
        self.assertEqual('EAS503', value)

    @weight(2)
    @visibility('visible')
    @number("7")
    def test_ex7(self):
        value = self.homework1.ex7()
        self.assertEqual(True, value)

    @weight(2)
    @visibility('visible')
    @number("8")
    def test_ex8(self):
        value = self.homework1.ex8()
        self.assertEqual(False, value)

    @weight(2)
    @visibility('visible')
    @number("9")
    def test_ex9(self):
        value = self.homework1.ex9()
        self.assertEqual('b', value)

    @weight(2)
    @visibility('visible')
    @number("10")
    def test_ex10(self):
        value = self.homework1.ex10()
        self.assertEqual(25, value)

    @weight(2)
    @visibility('visible')
    @number("11")
    def test_ex11(self):
        value = self.homework1.ex11()
        self.assertEqual(404, value)

    @weight(2)
    @visibility('visible')
    @number("12")
    def test_ex12(self):
        value = self.homework1.ex12()
        self.assertEqual(0, value)

    @weight(2)
    @visibility('visible')
    @number("13")
    def test_ex13(self):
        value = self.homework1.ex13()
        self.assertEqual(7.2, value)

    @weight(2)
    @visibility('visible')
    @number("14")
    def test_ex14(self):
        value = self.homework1.ex14()
        self.assertEqual(7, value)

    @weight(2)
    @visibility('visible')
    @number("15")
    def test_ex15(self):
        value = self.homework1.ex15()
        self.assertEqual(113.04, value)

    @weight(2)
    @visibility('visible')
    @number("16")
    def test_ex16(self):
        value = self.homework1.ex16()
        self.assertEqual(19.444444444444443, value)

    @weight(2)
    @visibility('visible')
    @number("17")
    def test_ex17(self):
        value = self.homework1.ex17()
        self.assertEqual('E', value)

    @weight(2)
    @visibility('visible')
    @number("18")
    def test_ex18(self):
        value = self.homework1.ex18()
        self.assertEqual('S', value)

    @weight(2)
    @visibility('visible')
    @number("19")
    def test_ex19(self):
        value = self.homework1.ex19()
        self.assertEqual('3', value)

    @weight(2)
    @visibility('visible')
    @number("20")
    def test_ex20(self):
        value = self.homework1.ex20()
        self.assertEqual(3, value)

    @weight(2)
    @visibility('visible')
    @number("21")
    def test_ex21(self):
        value = self.homework1.ex21()
        self.assertEqual(3.14159, value)

    @weight(2)
    @visibility('visible')
    @number("22")
    def test_ex22(self):
        value = self.homework1.ex22()
        self.assertEqual(str, value)

    @weight(2)
    @visibility('visible')
    @number("23")
    def test_ex23(self):
        value = self.homework1.ex23()
        self.assertEqual(float, value)

    @weight(2)
    @visibility('visible')
    @number("24")
    def test_ex24(self):
        value = self.homework1.ex24()
        self.assertEqual(True, value)

    @weight(2)
    @visibility('visible')
    @number("25")
    def test_ex25(self):
        value = self.homework1.ex25()
        self.assertEqual(True, value)

    @weight(2)
    @visibility('visible')
    @number("26")
    def test_ex26(self):
        value = self.homework1.ex26()
        self.assertEqual(7.5, value)

    @weight(2)
    @visibility('visible')
    @number("27")
    def test_ex27(self):
        filename = 'ex1_input.txt'
        value = self.homework1.ex27(filename)
        self.assertEqual(357, value)

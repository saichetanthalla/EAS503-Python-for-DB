import unittest

import assignment3
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment3(unittest.TestCase):
    def setUp(self):
        self.assignment3 = assignment3

    @weight(3)
    @visibility('visible')
    @number("1.1")
    def test_ex1_1(self):
        value = self.assignment3.ex1(40, 25)
        self.assertEqual(1000, value)

    @weight(3)
    @visibility('visible')
    @number("1.2")
    def test_ex1_2(self):
        value = self.assignment3.ex1(65, 63.4)
        self.assertEqual(4913.5, value)

    @weight(3)
    @visibility('visible')
    @number("1.3")
    def test_ex1_3(self):
        value = self.assignment3.ex1(20, 45)
        self.assertEqual(900, value)

    @weight(3)
    @visibility('visible')
    @number("1.4")
    def test_ex1_4(self):
        value = self.assignment3.ex1(55, 35.5)
        self.assertEqual(2218.75, value)

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_ex2_1(self):
        value = self.assignment3.ex2(0)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_ex2_2(self):
        value = self.assignment3.ex2(1)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("2.3")
    def test_ex2_3(self):
        value = self.assignment3.ex2(2)
        self.assertEqual('D', value)

    @weight(3)
    @visibility('visible')
    @number("2.4")
    def test_ex2_4(self):
        value = self.assignment3.ex2(3)
        self.assertEqual('C', value)

    @weight(3)
    @visibility('visible')
    @number("2.5")
    def test_ex2_5(self):
        value = self.assignment3.ex2(4)
        self.assertEqual('B', value)

    @weight(3)
    @visibility('visible')
    @number("2.6")
    def test_ex2_6(self):
        value = self.assignment3.ex2(5)
        self.assertEqual('A', value)

    @weight(3)
    @visibility('visible')
    @number("3.1")
    def test_ex3_1(self):
        value = self.assignment3.ex3(55)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("3.2")
    def test_ex3_2(self):
        value = self.assignment3.ex3(35)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("3.3")
    def test_ex3_3(self):
        value = self.assignment3.ex3(65)
        self.assertEqual('D', value)

    @weight(3)
    @visibility('visible')
    @number("3.4")
    def test_ex3_4(self):
        value = self.assignment3.ex3(73)
        self.assertEqual('C', value)

    @weight(3)
    @visibility('visible')
    @number("3.5")
    def test_ex3_5(self):
        value = self.assignment3.ex3(87)
        self.assertEqual('B', value)

    @weight(3)
    @visibility('visible')
    @number("3.6")
    def test_ex3_6(self):
        value = self.assignment3.ex3(92)
        self.assertEqual('A', value)

    @weight(3)
    @visibility('visible')
    @number("3.7")
    def test_ex3_7(self):
        value = self.assignment3.ex3(45)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("3.8")
    def test_ex3_8(self):
        value = self.assignment3.ex3(25)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("3.9")
    def test_ex3_9(self):
        value = self.assignment3.ex3(68)
        self.assertEqual('D', value)

    @weight(3)
    @visibility('visible')
    @number("3.10")
    def test_ex3_10(self):
        value = self.assignment3.ex3(77)
        self.assertEqual('C', value)

    @weight(3)
    @visibility('visible')
    @number("3.11")
    def test_ex3_11(self):
        value = self.assignment3.ex3(83)
        self.assertEqual('B', value)

    @weight(3)
    @visibility('visible')
    @number("3.12")
    def test_ex3_12(self):
        value = self.assignment3.ex3(96)
        self.assertEqual('A', value)

    @weight(3)
    @visibility('visible')
    @number("4.1")
    def test_ex4_1(self):
        value = self.assignment3.ex4(6)
        self.assertEqual('Freshman', value)

    @weight(3)
    @visibility('visible')
    @number("4.2")
    def test_ex4_2(self):
        value = self.assignment3.ex4(13)
        self.assertEqual('Sophomore', value)

    @weight(3)
    @visibility('visible')
    @number("4.3")
    def test_ex4_3(self):
        value = self.assignment3.ex4(23)
        self.assertEqual('Junior', value)

    @weight(3)
    @visibility('visible')
    @number("4.4")
    def test_ex4_4(self):
        value = self.assignment3.ex4(45)
        self.assertEqual('Senior', value)

    @weight(3)
    @visibility('visible')
    @number("4.5")
    def test_ex4_5(self):
        value = self.assignment3.ex4(3)
        self.assertEqual('Freshman', value)

    @weight(3)
    @visibility('visible')
    @number("4.6")
    def test_ex4_6(self):
        value = self.assignment3.ex4(15)
        self.assertEqual('Sophomore', value)

    @weight(3)
    @visibility('visible')
    @number("4.7")
    def test_ex4_7(self):
        value = self.assignment3.ex4(20)
        self.assertEqual('Junior', value)

    @weight(3)
    @visibility('visible')
    @number("4.8")
    def test_ex4_8(self):
        value = self.assignment3.ex4(35)
        self.assertEqual('Senior', value)

    @weight(3)
    @visibility('visible')
    @number("5.1")
    def test_ex5_1(self):
        value = self.assignment3.ex5(55, 85)
        self.assertEqual(200, value)

    @weight(3)
    @visibility('visible')
    @number("5.2")
    def test_ex5_2(self):
        value = self.assignment3.ex5(55, 45)
        self.assertEqual('Legal', value)

    @weight(3)
    @visibility('visible')
    @number("5.3")
    def test_ex5_3(self):
        value = self.assignment3.ex5(55, 100)
        self.assertEqual(475, value)

    @weight(3)
    @visibility('visible')
    @number("5.4")
    def test_ex5_4(self):
        value = self.assignment3.ex5(55, 75)
        self.assertEqual(150, value)

    @weight(3)
    @visibility('visible')
    @number("5.5")
    def test_ex5_5(self):
        value = self.assignment3.ex5(55, 35)
        self.assertEqual('Legal', value)

    @weight(3)
    @visibility('visible')
    @number("5.6")
    def test_ex5_6(self):
        value = self.assignment3.ex5(55, 120)
        self.assertEqual(575, value)

    @weight(3)
    @visibility('visible')
    @number("6.1")
    def test_ex6_1(self):
        value = self.assignment3.ex6('Kayak')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("6.2")
    def test_ex6_2(self):
        value = self.assignment3.ex6('Rotator')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("6.3")
    def test_ex6_3(self):
        value = self.assignment3.ex6('AACA')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("6.4")
    def test_ex6_4(self):
        value = self.assignment3.ex6('Stats')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("6.5")
    def test_ex6_5(self):
        value = self.assignment3.ex6('Madam')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("6.6")
    def test_ex6_6(self):
        value = self.assignment3.ex6('Test1234')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("7.1")
    def test_ex7_1(self):
        value = self.assignment3.ex7('March', 21)
        self.assertEqual('Spring', value)

    @weight(3)
    @visibility('visible')
    @number("7.2")
    def test_ex7_2(self):
        value = self.assignment3.ex7('June', 21)
        self.assertEqual('Summer', value)

    @weight(3)
    @visibility('visible')
    @number("7.3")
    def test_ex7_3(self):
        value = self.assignment3.ex7('November', 21)
        self.assertEqual('Fall', value)

    @weight(3)
    @visibility('visible')
    @number("7.4")
    def test_ex7_4(self):
        value = self.assignment3.ex7('January', 21)
        self.assertEqual('Winter', value)

    @weight(3)
    @visibility('visible')
    @number("7.5")
    def test_ex7_5(self):
        value = self.assignment3.ex7('April', 21)
        self.assertEqual('Spring', value)

    @weight(3)
    @visibility('visible')
    @number("7.6")
    def test_ex7_6(self):
        value = self.assignment3.ex7('July', 21)
        self.assertEqual('Summer', value)

    @weight(3)
    @visibility('visible')
    @number("7.7")
    def test_ex7_7(self):
        value = self.assignment3.ex7('September', 21)
        self.assertEqual('Summer', value)

    @weight(3)
    @visibility('visible')
    @number("7.8")
    def test_ex7_8(self):
        value = self.assignment3.ex7('October', 21)
        self.assertEqual('Fall', value)

    @weight(3)
    @visibility('visible')
    @number("8.1")
    def test_ex8_1(self):
        value = self.assignment3.ex8(1800)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("8.2")
    def test_ex8_2(self):
        value = self.assignment3.ex8(1900)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("8.3")
    def test_ex8_3(self):
        value = self.assignment3.ex8(1600)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("8.4")
    def test_ex8_4(self):
        value = self.assignment3.ex8(2000)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("9.1")
    def test_ex9_1(self):
        value = self.assignment3.ex9(5, 24, 1962)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("9.2")
    def test_ex9_2(self):
        value = self.assignment3.ex9(9, 31, 2000)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("9.3")
    def test_ex9_3(self):
        value = self.assignment3.ex9(2, 29, 2000)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("9.4")
    def test_ex9_4(self):
        value = self.assignment3.ex9(2, 29, 1800)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("10.1")
    def test_ex10_1(self):
        value = self.assignment3.ex10(9, 31, 2000)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("10.2")
    def test_ex10_2(self):
        value = self.assignment3.ex10(2, 13, 2020)
        self.assertEqual(44, value)

    @weight(3)
    @visibility('visible')
    @number("10.3")
    def test_ex10_3(self):
        value = self.assignment3.ex10(2, 29, 1800)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("10.4")
    def test_ex10_4(self):
        value = self.assignment3.ex10(7, 26, 2020)
        self.assertEqual(208, value)

    @weight(3)
    @visibility('visible')
    @number("11.1")
    def test_ex11_1(self):
        value = self.assignment3.ex11('ABC123')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("11.2")
    def test_ex11_2(self):
        value = self.assignment3.ex11('GHE952')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("11.3")
    def test_ex11_3(self):
        value = self.assignment3.ex11('1934ABT')
        self.assertEqual('Newer/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("11.4")
    def test_ex11_4(self):
        value = self.assignment3.ex11('bTR342')
        self.assertEqual('Invalid', value)

    @weight(3)
    @visibility('visible')
    @number("11.5")
    def test_ex11_5(self):
        value = self.assignment3.ex11('MHR621')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("11.6")
    def test_ex11_6(self):
        value = self.assignment3.ex11('POR208')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("11.7")
    def test_ex11_7(self):
        value = self.assignment3.ex11('1972BNT')
        self.assertEqual('Newer/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("11.8")
    def test_ex11_8(self):
        value = self.assignment3.ex11('cRA542')
        self.assertEqual('Invalid', value)

    @weight(3)
    @visibility('visible')
    @number("12.1")
    def test_ex12_1(self):
        value = self.assignment3.ex12('06/10/1960')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("12.2")
    def test_ex12_2(self):
        value = self.assignment3.ex12('06/08/1948')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("12.3")
    def test_ex12_3(self):
        value = self.assignment3.ex12('05/08/1940')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("12.4")
    def test_ex12_4(self):
        value = self.assignment3.ex12('03/12/1948')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("12.5")
    def test_ex12_5(self):
        value = self.assignment3.ex12('02/12/1956')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("12.6")
    def test_ex12_6(self):
        value = self.assignment3.ex12('12/12/1990')
        self.assertEqual(False, value)

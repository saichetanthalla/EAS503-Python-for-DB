import unittest

import assignment2
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment2(unittest.TestCase):
    def setUp(self):
        self.assignment2 = assignment2

    @weight(3)
    @visibility('visible')
    @number("1.1")
    def test_ex1_1(self):
        value = self.assignment2.ex1('Brian')
        self.assertEqual('Hello, Brian, nice to meet you!', value)

    @weight(3)
    @visibility('visible')
    @number("1.2")
    def test_ex1_2(self):
        value = self.assignment2.ex1('John')
        self.assertEqual('Hello, John, nice to meet you!', value)

    @weight(3)
    @visibility('visible')
    @number("1.3")
    def test_ex1_3(self):
        value = self.assignment2.ex1('Jane')
        self.assertEqual('Hello, Jane, nice to meet you!', value)

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_ex2_1(self):
        value = self.assignment2.ex2(1, 2, 3)
        self.assertEqual(
            'The value of x is: 1.\nThe value of y is: 2.\nThe value of z is: 3.', value)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_ex2_2(self):
        value = self.assignment2.ex2(40, 50, 60)
        self.assertEqual(
            'The value of x is: 40.\nThe value of y is: 50.\nThe value of z is: 60.', value)

    @weight(3)
    @visibility('visible')
    @number("3.1")
    def test_ex3_1(self):
        value = self.assignment2.ex3(45.23, 89.34)
        self.assertEqual(
            'The area of a rectangle with length 45.23 and width 89.34 is 4040.85.', value)

    @weight(3)
    @visibility('visible')
    @number("3.2")
    def test_ex3_2(self):
        value = self.assignment2.ex3(40.90, 50.55)
        self.assertEqual(
            'The area of a rectangle with length 40.9 and width 50.55 is 2067.49.', value)

    @weight(3)
    @visibility('visible')
    @number("4.1")
    def test_ex4_1(self):
        value = self.assignment2.ex4(15)
        self.assertEqual(2827.43, value)

    @weight(3)
    @visibility('visible')
    @number("4.2")
    def test_ex4_2(self):
        value = self.assignment2.ex4(7.25)
        self.assertEqual(660.52, value)

    @weight(3)
    @visibility('visible')
    @number("4.3")
    def test_ex4_3(self):
        value = self.assignment2.ex4(5.25)
        self.assertEqual(346.36, value)

    @weight(3)
    @visibility('visible')
    @number("4.4")
    def test_ex4_4(self):
        value = self.assignment2.ex4(17.25)
        self.assertEqual(3739.28, value)

    @weight(3)
    @visibility('visible')
    @number("5.1")
    def test_ex5_1(self):
        value = self.assignment2.ex5(15)
        self.assertEqual(14137.17, value)

    @weight(3)
    @visibility('visible')
    @number("5.2")
    def test_ex5_2(self):
        value = self.assignment2.ex5(7.5)
        self.assertEqual(1767.15, value)

    @weight(3)
    @visibility('visible')
    @number("5.3")
    def test_ex5_3(self):
        value = self.assignment2.ex5(78.2)
        self.assertEqual(2003128.77, value)

    @weight(3)
    @visibility('visible')
    @number("5.4")
    def test_ex5_4(self):
        value = self.assignment2.ex5(8.2)
        self.assertEqual(2309.56, value)

    @weight(3)
    @visibility('visible')
    @number("6.1")
    def test_ex6_1(self):
        value = self.assignment2.ex6(150, 65)
        self.assertEqual(25.56, value)

    @weight(3)
    @visibility('visible')
    @number("6.2")
    def test_ex6_2(self):
        value = self.assignment2.ex6(110, 55)
        self.assertEqual(26.18, value)

    @weight(3)
    @visibility('visible')
    @number("7.1")
    def test_ex7_1(self):
        value = self.assignment2.ex7(20, 50)
        self.assertEqual('The refund amount is $14.50.', value)

    @weight(3)
    @visibility('visible')
    @number("7.2")
    def test_ex7_2(self):
        value = self.assignment2.ex7(67, 59)
        self.assertEqual('The refund amount is $21.45.', value)

    @weight(3)
    @visibility('visible')
    @number("8.1")
    def test_ex8_1(self):
        value = self.assignment2.ex8(10, 5)
        expected_result = """The sum of 10 and 5 is 15.
The difference when 5 is subtracted from 10 is 5.
The product of 10 and 5 is 50.
The quotient when 10 is divided by 5 is 2.
The remainder when 10 is divided by 5 is 0.
The result of 10^5 is 100000."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("8.2")
    def test_ex8_2(self):
        value = self.assignment2.ex8(6, 5)
        expected_result = """The sum of 6 and 5 is 11.
The difference when 5 is subtracted from 6 is 1.
The product of 6 and 5 is 30.
The quotient when 6 is divided by 5 is 1.
The remainder when 6 is divided by 5 is 1.
The result of 6^5 is 7776."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("9.1")
    def test_ex9_1(self):
        value = self.assignment2.ex9(1500, 4.3, 4)
        self.assertEqual(
            'After 4 years at 4.3%, the investment will be worth $1758.00.', value)

    @weight(3)
    @visibility('visible')
    @number("9.2")
    def test_ex9_2(self):
        value = self.assignment2.ex9(150000, 6.5, 30)
        self.assertEqual(
            'After 30 years at 6.5%, the investment will be worth $442500.00.', value)

    @weight(3)
    @visibility('visible')
    @number("10.1")
    def test_ex10_1(self):
        value = self.assignment2.ex10(1500, 4.3, 6, 4)
        self.assertEqual(
            '$1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.', value)

    @weight(3)
    @visibility('visible')
    @number("10.2")
    def test_ex10_2(self):
        value = self.assignment2.ex10(150000, 6.5, 30, 12)
        self.assertEqual(
            '$150000 invested at 6.5% for 30 years compounded 12 times per year is $1048769.70.', value)

    @weight(3)
    @visibility('visible')
    @number("11.1")
    def test_ex11_1(self):
        value = self.assignment2.ex11('Buffalo')
        self.assertEqual("The input string 'Buffalo' has 7 characters.", value)

    @weight(3)
    @visibility('visible')
    @number("11.2")
    def test_ex11_2(self):
        value = self.assignment2.ex11('University at Buffalo')
        self.assertEqual(
            "The input string 'University at Buffalo' has 21 characters.", value)

    @weight(3)
    @visibility('visible')
    @number("11.3")
    def test_ex11_3(self):
        value = self.assignment2.ex11(
            'Center for Computational Research (CCR)')
        self.assertEqual(
            "The input string 'Center for Computational Research (CCR)' has 39 characters.", value)

    @weight(3)
    @visibility('visible')
    @number("12.1")
    def test_ex12_1(self):
        value = self.assignment2.ex12('dog', 'walk', 'blue', 'quickly')
        self.assertEqual(
            "Do you walk your blue dog quickly? That's hilarious!", value)

    @weight(3)
    @visibility('visible')
    @number("12.2")
    def test_ex12_2(self):
        value = self.assignment2.ex12('cat', 'walk', 'brown', 'slowly')
        self.assertEqual(
            "Do you walk your brown cat slowly? That's hilarious!", value)

    @weight(3)
    @visibility('visible')
    @number("13.1")
    def test_ex13_1(self):
        value = self.assignment2.ex13(25, 65, 2015)
        expected_result = """Your current age is: 25.
You would like to retire at: 65.
You have 40 years left until you can retire.
It's 2015, so you can retire in 2055."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("13.2")
    def test_ex13_2(self):
        value = self.assignment2.ex13(36, 72, 2021)
        expected_result = """Your current age is: 36.
You would like to retire at: 72.
You have 36 years left until you can retire.
It's 2021, so you can retire in 2057."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("14.1")
    def test_ex14_1(self):
        value = self.assignment2.ex14(15, 20)
        expected_result = """The length of the room in feet is 15.
The width of the room in feet is 20.
The dimension of the room is 15 by 20 feet.
The area is
300 square feet
27.87 square meters"""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("14.2")
    def test_ex14_2(self):
        value = self.assignment2.ex14(45, 35)
        expected_result = """The length of the room in feet is 45.
The width of the room in feet is 35.
The dimension of the room is 45 by 35 feet.
The area is
1575 square feet
146.32 square meters"""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("15.1")
    def test_ex15_1(self):
        value = self.assignment2.ex15(8, 2)
        expected_result = """There are 8 with 2 pizzas.
Each person gets 2 pieces of pizza.
There are 0 leftover pieces."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("15.2")
    def test_ex15_2(self):
        value = self.assignment2.ex15(20, 6)
        expected_result = """There are 20 with 6 pizzas.
Each person gets 2 pieces of pizza.
There are 8 leftover pieces."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("16.1")
    def test_ex16_1(self):
        value = self.assignment2.ex16(12, 30)
        expected_result = 'You will need to purchase 2 gallons of paint to cover 360 square feet.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("16.2")
    def test_ex16_2(self):
        value = self.assignment2.ex16(25, 35)
        expected_result = 'You will need to purchase 3 gallons of paint to cover 875 square feet.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("17.1")
    def test_ex17_1(self):
        value = self.assignment2.ex17(3.14159)
        expected_result = 'The value is: 3.1416.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("17.2")
    def test_ex17_2(self):
        value = self.assignment2.ex17(1.61803398875)
        expected_result = 'The value is: 1.6180.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("18.1")
    def test_ex18_1(self):
        value = self.assignment2.ex18(3.14159)
        expected_result = 'The value is:     3.1416.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("18.2")
    def test_ex18_2(self):
        value = self.assignment2.ex18(1.61803398875)
        expected_result = 'The value is:     1.6180.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("19.1")
    def test_ex19_1(self):
        value = self.assignment2.ex19(3.14159)
        expected_result = 'The value is: 3.141590--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("19.2")
    def test_ex19_2(self):
        value = self.assignment2.ex19(1.61803398875)
        expected_result = 'The value is: 1.618034--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("20.1")
    def test_ex20_1(self):
        value = self.assignment2.ex20(3.14159)
        expected_result = 'The value is: --3.141590--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("20.2")
    def test_ex20_2(self):
        value = self.assignment2.ex20(1.61803398875)
        expected_result = 'The value is: --1.618034--.'
        self.assertEqual(expected_result, value)

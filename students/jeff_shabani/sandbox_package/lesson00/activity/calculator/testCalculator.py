#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import MagicMock

from UW.Adv_Klass.students.jeff_shabani.import Adder
from UW.Adv_Klass.students.jeff_shabani.lesson01.activity.calculator.subtracter import Subtracter
from UW.Adv_Klass.students.jeff_shabani.lesson01.activity.calculator.divider import Divider
from UW.Adv_Klass.students.jeff_shabani.lesson01.activity.calculator.multiplier import Multiplier
from UW.Adv_Klass.students.jeff_shabani.lesson01.activity.calculator.calculator import Calculator
from UW.Adv_Klass.students.jeff_shabani.lesson01.activity.calculator.exceptions import InsufficientOperands

class AdderTests(TestCase):

    def test_adding(self):
        adder = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtractorTests(TestCase):

    def test_subtracting(self):
        subtractir = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtractir.calc(i, j))

class CalculatorTests(TestCase):

    def setUp(self):
        self.adder = Adder()
        self.subtractor = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()

        self.calculator = Calculator(self.adder, self.subtractor, self.multiplier, self.divider)

    def test_insufficient_operands(self):
        self.calculator.enter_number(0)

        with self.assertRaises(InsufficientOperands):
            self.calculator.add()


    def test_adder_call(self):
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(2)
        self.calculator.enter_number(1)
        self.calculator.add()

        self.adder.calc.assert_called_with(1,2)

    def test_subtractor_call(self):
        self.subtractor.calc = MagicMock(return_value=0)

        self.calculator.enter_number(2)
        self.calculator.enter_number(1)
        self.calculator.subtract()

        self.subtractor.calc.assert_called_with(1,2)


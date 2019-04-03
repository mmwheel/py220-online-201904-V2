#!/usr/bin/env python3
'''
Our calculator
'''
from exceptions import InsufficientOperands


class Calculator():
    '''
    Class base for the calculator
    '''

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        '''
        What it says on the tin.  Enter a number.
        '''
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        '''
        Shortcut to operations on numbers.  Keeps from having to repeat whole
        functions.
        '''
        try:
            result = operator.calc(self.stack[1], self.stack[0])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        '''
        Addition method
        '''
        return self._do_calc(self.adder)

    def subtract(self):
        '''
        Subtraction method
        '''
        return self._do_calc(self.subtracter)

    def multiply(self):
        '''
        Multiplication method
        '''
        return self._do_calc(self.multiplier)

    def divide(self):
        '''
        Division method
        '''
        return self._do_calc(self.divider)

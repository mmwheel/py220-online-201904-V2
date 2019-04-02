#!/usr/bin/env python3
'''
Squaring module for our calculator
'''
class Squarer():
    '''
    A simple squaring function
    '''

    @staticmethod
    def calc(operand):
        '''
        calculating the square
        '''
        #return operand**2        # OLD
        #return operand**operand  # BAD
        return operand*operand   # This should work

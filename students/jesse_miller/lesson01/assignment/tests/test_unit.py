#!/usr/bin/env python3
'''
Testing methods for first lesson in Python220
'''
import sys
sys.path.append('../inventory_management/')
import main
from electric_appliances import ElectricAppliances
import home_furniture
import market_prices
import store_inventory
'''
I tried just importing the directory, but no love.
'''
from unittest import TestCase
from unittest.mock import Mock, MagicMock

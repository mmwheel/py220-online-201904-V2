""" Pytest cases for inventory management classes """

# Douglas Klos
# April 3rd, 2019
# Python 220, Lesson 01
# test_unit.py

from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management.market_prices import get_latest_price


def test_init_inventory():
    """
    Tests that inventory class initializes correctly
    """
    product_dict = {}
    product_dict['product_code'] = 100
    product_dict['description'] = 'Chair'
    product_dict['market_price'] = 200
    product_dict['rental_price'] = 50

    inventory = Inventory(**product_dict)

    print(inventory.return_as_dictionary())
    print(product_dict)

    assert inventory.product_code == product_dict['product_code']
    assert inventory.description == product_dict['description']
    assert inventory.market_price == product_dict['market_price']
    assert inventory.rental_price == product_dict['rental_price']


def test_return_as_dict_inventory():
    """
    Tests that inventory class returns the expected dictionary
    """
    product_dict = {}
    product_dict['product_code'] = 100
    product_dict['description'] = 'Chair'
    product_dict['market_price'] = 200
    product_dict['rental_price'] = 50

    inventory = Inventory(**product_dict)

    print(inventory.return_as_dictionary())
    print(product_dict)

    assert product_dict == inventory.return_as_dictionary()


def test_init_furniture():
    """
    Tests that furniture class initializes correctly
    """
    product_dict = {}
    product_dict['product_code'] = 100
    product_dict['description'] = 'Chair'
    product_dict['market_price'] = 200
    product_dict['rental_price'] = 50
    product_dict['material'] = 'Leather'
    product_dict['size'] = 'L'

    chair = Furniture(**product_dict)

    print(chair.return_as_dictionary())
    print(product_dict)

    assert chair.product_code == product_dict['product_code']
    assert chair.description == product_dict['description']
    assert chair.market_price == product_dict['market_price']
    assert chair.rental_price == product_dict['rental_price']
    assert chair.material == product_dict['material']
    assert chair.size == product_dict['size']


def test_return_as_dict_furniture():
    """
    Tests that furniture class returns the expected dictionary
    """
    product_dict = {}
    product_dict['product_code'] = 100
    product_dict['description'] = 'Chair'
    product_dict['market_price'] = 200
    product_dict['rental_price'] = 50
    product_dict['material'] = 'Leather'
    product_dict['size'] = 'L'

    chair = Furniture(**product_dict)

    print(chair.return_as_dictionary())
    print(product_dict)

    assert product_dict == chair.return_as_dictionary()


def test_init_appliance():
    """
    Tests that electric appliance class initializes correctly
    """
    product_dict = {}
    product_dict['product_code'] = 8942
    product_dict['description'] = 'Oven'
    product_dict['market_price'] = 600
    product_dict['rental_price'] = 200
    product_dict['brand'] = 'Topf and Sons'
    product_dict['voltage'] = 230

    oven = ElectricAppliances(**product_dict)

    print(oven.return_as_dictionary())
    print(product_dict)

    assert oven.product_code == product_dict['product_code']
    assert oven.description == product_dict['description']
    assert oven.market_price == product_dict['market_price']
    assert oven.rental_price == product_dict['rental_price']
    assert oven.brand == product_dict['brand']
    assert oven.voltage == product_dict['voltage']


def test_return_as_dict_appliance():
    """
    Tests that electric appliance class returns the expected dictionary
    """
    product_dict = {}
    product_dict['product_code'] = 8942
    product_dict['description'] = 'Oven'
    product_dict['market_price'] = 600
    product_dict['rental_price'] = 200
    product_dict['brand'] = 'Topf and Sons'
    product_dict['voltage'] = 230

    oven = ElectricAppliances(**product_dict)

    print(oven.return_as_dictionary())
    print(product_dict)

    assert product_dict == oven.return_as_dictionary()


def test_get_latest_price_market():
    """
    Tests that get latest price returns the expected value.
    In this case, the expected value is what we pass in.
    The function is very broken.
    """
    assert get_latest_price(100) == 100
    assert get_latest_price(1000) == 1000
    assert get_latest_price(-100) == -100
    assert get_latest_price(-1000) == -1000

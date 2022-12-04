import pytest


@pytest.fixture
#@pytest.yield_fixture
def setup():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close Browser")


def testAddItemtoCart(setup):
    print("Add item to cart")


def testRemoveItemFromCart(setup):
    print("Remove item successful")

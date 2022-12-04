import pytest

@pytest.mark.skip
def testlogin():
    print("login successfully")

@pytest.mark.regression
def testLogOff():
    print("Logoff successful")

@pytest.mark.sanity
def testCalculation():
    assert 2+2 == 4

@pytest.mark.xfail
def testCalculation1():
    assert 2+2 == 5
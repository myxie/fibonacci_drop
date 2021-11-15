import pytest

from fibonacci_drop import FibonacciAppDrop, MyDataDROP

given = pytest.mark.parametrize


def test_myApp_class():
    assert FibonacciAppDrop("a", "a").run() == 196418


def test_myData_class():
    assert MyDataDROP("a", "a").getIO() == "Hello from MyDataDROP"


def test_myData_dataURL():
    assert MyDataDROP("a", "a").dataURL == "Hello from the dataURL method"

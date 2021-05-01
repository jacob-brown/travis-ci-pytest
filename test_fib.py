import pytest
import fibonacci


def test_fib_10():
    assert fibonacci.fibonacci(10) == 55


def test_fib_not_20():
    assert fibonacci.fibonacci(20) != 20


def test_returnTen():
    assert fibonacci.returnTen() == 10
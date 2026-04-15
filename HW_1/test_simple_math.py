from simple_math import SimpleMath
import pytest

@pytest.fixture
def test():
    return SimpleMath()
#  для метода square
def test_square_positive(test):
    assert test.square(2) == 4

def test_square_negative(test):
    assert test.square(-2) == 4

def test_square_zero(test):
    assert test.square(0) == 0

#  для метода cube
def test_cube_positive(test):
    assert test.cube(3) == 27

def test_cube_negative(test):
    assert test.cube(-3) == -27

def test_cube_zero(test):
    assert test.cube(0) == 0



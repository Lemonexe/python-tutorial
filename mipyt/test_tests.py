# more advanced testing using pytest
# pytest will find the file because it is named test_*.py

import pytest
from math import sin, pi

# pytest will find the function because it is named test_*
def test_sin():
    assert abs(sin(pi)) < 1e-6

def faulty_function():
    raise SystemExit(1)

# assert is the standard keyword, but for testing errors we need to do this:
def test_raise():
    with pytest.raises(SystemExit):
        faulty_function()

# call the same function with multiple different parameters, the value is injected as 'x'
def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize('n', range(0, 1000, 2)) # wow that's a lot of tests!
def test_periodicity(n):
    assert is_even(n)
    assert not is_even(n+1)

# if I need multiple, it is parametrize(['x', 'y', 'z'], [(1,2,3), (4,5,6)])

# let's create a fixture – some intermediate that I have to calculate before a test
# often a database connection, or an internal api reponse, those things
class Client:
    asdf = 1234

@pytest.fixture
def client():
    return Client()

def test_fixture(client): # param must be named exactly same as the fixture
    assert hasattr(client, 'asdf')

# for HTTP requests we need betamax - like VCR cassettes in ruby

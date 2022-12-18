# python -m pip install pytest

import pytest

def secti(a, b):
    """Vrátí součet dvou čísel"""
    return a + b

def test_secti():
    """Otestuje funkci secti"""
    assert secti(1, 2) == 3
    with pytest.raises(TypeError):
        secti(1, 'asdf')

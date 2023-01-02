"""Tests operation method"""
from battle_ship.operations import Operations
from battle_ship.exceptions import OutOfBounds
import pytest


def test_addtion():
    """Adds two tuples"""
    with pytest.raises(OutOfBounds):
        Operations.addition((0,10), (0,1))

def test_subtraction():
    """Subtracts two tuples"""
    with pytest.raises(OutOfBounds):
        Operations.subtraction((1,0), (10,0))

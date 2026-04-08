"""
Program Name: Rotation Utils Tests
Author: Farouk Bellili
Purpose: This program contains pytest unit tests for the adjust_rotation
         function from rotation_utils.py to do the testing
Starter Code: rotation_utils.py
Date: April 7, 2026
"""

import pytest
from rotation_utils import adjust_rotation


def test_positive_value():
    assert adjust_rotation(100) == 100


def test_large_positive_value():
    assert adjust_rotation(460) == 100


def test_larger_positive_value():
    assert adjust_rotation(820) == 100


def test_negative_value():
    assert adjust_rotation(-100) == 260


def test_large_negative_value():
    assert adjust_rotation(-460) == 260


def test_larger_negative_value():
    assert adjust_rotation(-820) == 260


def test_type_error():
    with pytest.raises(TypeError):
        adjust_rotation("ABC")


def test_zero():
    assert adjust_rotation(0) == 0


def test_full_rotation():
    assert adjust_rotation(360) == 0


def test_float_value():
    assert adjust_rotation(100.5) == 100.5

"""
Program Name: Rotation Normalizer
Author: Kenneth Cherry
Purpose: Normalize rotation degrees to within a 0–359 range and verify correctness using pytest.
Date: November 9, 2025
"""
import pytest
def normalize_rotation(degrees):
    try:
        degrees = float(degrees)
        normalized = degrees % 360
        return normalized if normalized >= 0 else normalized + 360
    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric value.")

def test_normalize_rotation_positive():
    assert normalize_rotation(100) == 100
    assert normalize_rotation(460) == 100
    assert normalize_rotation(820) == 100

def test_normalize_rotation_negative():
    assert normalize_rotation(-100) == 260
    assert normalize_rotation(-460) == 260
    assert normalize_rotation(-820) == 260

def test_normalize_rotation_exception():
    with pytest.raises(ValueError):
        normalize_rotation("abc")
    with pytest.raises(ValueError):
        normalize_rotation(None)

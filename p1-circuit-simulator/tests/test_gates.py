import numpy as np
from qsim.state import zero_state, apply_1q
from qsim.gates import H, X, Z

# Tests on H gate
def test_h_on_zero_gives_equal_amplitudes():
    s = apply_1q(zero_state(1), H)
    expected = np.array([1, 1]) / np.sqrt(2)
    assert np.allclose(s, expected)

def test_h_twice_returns_to_zero():
    s = apply_1q(apply_1q(zero_state(1), H), H)
    assert np.allclose(s, zero_state(1))

# Test on X gate
def test_x_on_zero_gives_opposite_states():
    s = apply_1q(zero_state(1), X)
    expected = np.array([0, 1])
    assert np.allclose(s, expected)

def test_x_twice_returns_to_zero():
    s = apply_1q(apply_1q(zero_state(1), X), X)
    assert np.allclose(s, zero_state(1))

# Test of Z gate
def test_z_changes_phase():
    s = np.array([0, 1], dtype=complex)
    result = apply_1q(s, Z)
    expected = np.array([0, -1], dtype=complex)
    assert np.allclose(result, expected)

def test_z_on_zero_gives_zero():
    s = apply_1q(zero_state(1), Z)
    assert np.allclose(s, zero_state(1))

# Combination tests
def test_hzh_flips_zero_to_one():
    s = apply_1q(apply_1q(apply_1q(zero_state(1), H), Z), H)
    expected = np.array([0, 1], dtype=complex)
    assert np.allclose(s, expected)

def test_hxh_on_zero():
    s = apply_1q(apply_1q(apply_1q(zero_state(1), H), X), H)
    expected = zero_state(1) # hxh returns the same result as input
    assert np.allclose(s, expected)
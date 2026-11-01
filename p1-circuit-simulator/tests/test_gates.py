import numpy as np
from qsim.state import apply_gate_specific, zero_state, apply_1q, apply_gate_all
from qsim.gates import H, X, Y, Z, CNOT

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

# Test on Y gate
def test_y_on_zero():
    s = apply_1q(zero_state(1), Y)
    expected = np.array([0, 1j], dtype=complex)
    assert np.allclose(s, expected)

def test_y_on_zero_twice():
    state = np.array([0.8, 0.6], dtype=complex)
    s = apply_1q(apply_1q(state, Y), Y)
    assert np.allclose(s, state)

#? Combination tests
def test_hzh_flips_zero_to_one():
    s = apply_1q(apply_1q(apply_1q(zero_state(1), H), Z), H)
    expected = np.array([0, 1], dtype=complex)
    assert np.allclose(s, expected)

def test_hxh_on_zero():
    s = apply_1q(apply_1q(apply_1q(zero_state(1), H), X), H)
    expected = zero_state(1) # hxh returns the same result as input for |0|, acts as Z
    assert np.allclose(s, expected)

#? Tests for Kronecker Product
# apply_gate_all
def test_hadamard_two_qubit():
    s = apply_gate_all(zero_state(2), H)
    expected = np.array([1, 1, 1, 1], dtype=complex) / 2
    print(s)
    assert np.allclose(s, expected)

def test_hadamard_three_qubit():
    s = apply_gate_all(zero_state(3), H)
    expected = np.array([1 for item in range(8)], dtype=complex) / (np.sqrt(2) * 2)
    assert np.allclose(s, expected)

# apply_gate_specific
def test_hadamard_specific_two_qubit():
    s = apply_gate_specific(np.array([0, 1, 0, 0], dtype=complex), H, 1)
    expected = np.array([1, -1, 0, 0], dtype=complex) / np.sqrt(2)
    assert np.allclose(s, expected)

def test_hadamard_specific_three_qubit():
    state = np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype=complex)
    s = apply_gate_specific(state, H, 1)
    expected = np.array([1, 0, -1, 0, 0, 0, 0, 0], dtype=complex) / np.sqrt(2)
    assert np.allclose(s, expected)





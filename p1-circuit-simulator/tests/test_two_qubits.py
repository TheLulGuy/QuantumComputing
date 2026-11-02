import numpy as np
from qsim.gates import CNOT, H
from qsim.state import zero_state, apply_gate_fast, apply_gate_all, apply_gate_fast_specific
from tests.helpers import random_state, basis
import pytest
# CNOT gate tests
def test_cnot_10_to_11():
    s = np.array([0, 0, 1, 0], dtype=complex)
    expected = np.array([0, 0, 0, 1], dtype=complex)
    assert np.allclose(CNOT @ s, expected)

def test_cnot_keeps_first_qubit():
    s = np.array([1, 1, 0, 0], dtype=complex)
    assert np.allclose(CNOT @ s, s)

def test_cnot_bell_state():
    s = zero_state(2)
    result = apply_gate_fast_specific(s, H, 0)
    result = apply_gate_fast_specific(result, CNOT, [0, 1])
    expected = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    assert np.allclose(result, expected)

def test_cnot_fast_matches_matrix():
    s = random_state(2)
    assert np.allclose(apply_gate_fast(s, CNOT, [0, 1]), CNOT @ s)

# 2. Ordering: swapped roles, non-adjacent, control in the middle,
#    and cases where nothing should change
@pytest.mark.parametrize('bits, targets, expected_bits', [
    ("01", [1, 0], '11'),     # swapped roles flips
    ("10", [1, 0], '10'),     # swapped roles, control is 0: unchanged
    ("100", [0, 2], '101'),    # non-adjacent flips
    ("010", [0, 2], '010'),    # non-adjacent, control is 0: unchanged
    ("010", [1, 0], '110'),    # control in the middle
])
def test_cnot_target_ordering(bits, targets, expected_bits):
    result = apply_gate_fast_specific(basis(bits), CNOT, targets)
    assert np.allclose(result, basis(expected_bits))


@pytest.mark.parametrize('k', [0, 1, 2])
def test_specific_matches_fast(k):
    s = random_state(3)
    assert np.allclose(apply_gate_fast(s, H, [k]), apply_gate_fast_specific(s, H, k))



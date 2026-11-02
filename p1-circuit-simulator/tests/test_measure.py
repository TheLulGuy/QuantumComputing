import pytest
from qsim.state import zero_state, apply_gate_fast_specific
from qsim.measure import probabilities, marginal_probabilities, sample
from qsim.gates import H, CNOT
from tests.helpers import random_state, basis
import numpy as np

bell_state = apply_gate_fast_specific(zero_state(2), H, 0)
bell_state = apply_gate_fast_specific(bell_state, CNOT, [0, 1])

def test_probabilities_zero_state():
    s = zero_state(2)
    assert np.allclose(probabilities(s), s)

# Tests probability in bell state
def test_probabilities_bell_state():
    expected = np.array([0.5, 0, 0, 0.5])
    assert np.allclose(probabilities(bell_state), expected)

# Checks if the sum of probabilities in a random state give 1
def test_random_state_probability_unity():
    s = random_state(2)
    prob = probabilities(s)
    assert np.allclose(np.sum(prob), 1)


def test_sample_bell_only_00_and_11():
    counts = sample(bell_state, 1000, rng=0)
    assert set(counts) == {'00', '11'}
    assert sum(counts.values()) == 1000

def test_sample_same_seed_same_result():
    assert sample(bell_state, 1000, rng=1) == sample(bell_state, 1000, rng=1)

def test_marginal_basis_state():
    s = basis('10')
    assert np.allclose(marginal_probabilities(s, [0]), [0, 1])
    assert np.allclose(marginal_probabilities(s, [1]), [1, 0])


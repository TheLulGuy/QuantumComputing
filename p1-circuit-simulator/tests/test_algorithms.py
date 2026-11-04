import pytest
import numpy as np

from qsim.algorithms import dj_algorithmn, build_oracle, mcz_identity, grover, grover_circuit
from qsim.gates import CNOT
from qsim.measure import probabilities

def test_oracle_identity_is_cnot():
    assert np.allclose(build_oracle(lambda x:x, 1), CNOT)

@pytest.mark.parametrize('f, n', [
    (lambda x: 0, 2),
    (lambda x: (x & 1) ^ (x >> 1), 2),
    (lambda x: x % 2, 3), 
])
def test_oracle_is_its_own_inverse(f, n):
    U = build_oracle(f, n)
    assert np.allclose(U @ U, np.eye(2**(n+1)))

# 3. The algorithm gives the right verdict
@pytest.mark.parametrize('f, n, expected', [
    (lambda x: 0, 2, "Constant"),                     # constant
    (lambda x: 1, 2, "Constant"),                     # constant
    (lambda x: (x & 1) ^ (x >> 1), 2, "Balanced"),    # balanced
    (lambda x: x % 2, 3, "Balanced"),                 # balanced
])
def test_deutsch_jozsa(f, n, expected):
    assert dj_algorithmn(f, n) == expected

#? Tests for grover algorithm
# The stamp -1 on the allones state only
def test_mcz_stamps_only_all_ones():
    assert np.allclose(mcz_identity(2), np.diag([1, 1, 1, -1]))


# Grover finds every marked door(seeded for repetitiveness and debugability)
@pytest.mark.parametrize('marked', range(8))
def test_grover_finds_marked(marked):
    counts = grover(marked, 3, rng=0)
    assert max(counts, key=counts.get) == format(marked, '03b')


# Success probability is high at the default number of rounds.
@pytest.mark.parametrize('n', [2, 3, 4])
@pytest.mark.parametrize('marked_kind', ['first', 'last'])
def test_grover_success_probability(n, marked_kind):
    marked = 0 if marked_kind == 'first' else 2 ** n - 1
    state = grover_circuit(marked, n).run()
    assert probabilities(state)[marked] > 0.9
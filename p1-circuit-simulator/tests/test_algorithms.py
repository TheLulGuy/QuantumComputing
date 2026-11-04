import pytest
import numpy as np

from qsim.algorithms import dj_algorithmn, build_oracle
from qsim.gates import CNOT

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
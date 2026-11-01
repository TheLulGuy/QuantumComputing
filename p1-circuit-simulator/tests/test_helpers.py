from tests.helpers import basis
import numpy as np
from qsim.state import zero_state

def test_basis_index():
    assert basis("101")[5] == 1
    assert np.count_nonzero(basis("101")) == 1

def test_basis_matches_zero_state():
    assert np.allclose(basis("000"), zero_state(3))
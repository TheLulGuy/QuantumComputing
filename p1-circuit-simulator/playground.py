from qsim.state import *
from qsim.gates import *
from qsim.measure import *
from qsim.circuit import Circuit
import numpy as np
from qsim.algorithms import *

for item in range(10):
    print(grover(3, 3, rng=item))
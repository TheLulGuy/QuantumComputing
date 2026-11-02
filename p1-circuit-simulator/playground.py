from qsim.state import *
from qsim.gates import *
from qsim.circuit import Circuit
from pprint import pprint
c = Circuit(2).h(0).cx(0, 1).x(0).y(0).y(1).cx(0, 1)
pprint(c.operations)
print(c.depth())
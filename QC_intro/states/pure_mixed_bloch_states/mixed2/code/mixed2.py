#
# https://docs.quantum.ibm.com/api/qiskit/qiskit.visualization.plot_bloch_multivector
#


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
 
qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
 
# You can reverse the order of the qubits.
 
from qiskit.quantum_info import DensityMatrix
 
qc = QuantumCircuit(2)
qc.h([0, 1])
qc.t(1)
qc.s(0)
qc.cx(0,1)
 
matrix = DensityMatrix(qc)
plot_bloch_multivector(matrix, title='My Bloch Spheres', filename="slides/pure_mixed_bloch/results/bloch2", reverse_bits=True)



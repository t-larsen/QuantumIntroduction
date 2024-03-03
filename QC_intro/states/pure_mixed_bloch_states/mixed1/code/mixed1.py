#
# https://docs.quantum.ibm.com/api/qiskit/qiskit.visualization.plot_bloch_multivector
#


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
 
qc = QuantumCircuit(2)
qc.h(0)
qc.x(0)
 
state = Statevector(qc)
plot_bloch_multivector(state, filename="slides/pure_mixed_bloch/results/pure_mixed_bloch1")
#plot_bloch_multivector(matrix, title='My Bloch Spheres', filename="slides/pure_mixed_bloch/results/pure_mixed bloch1", reverse_bits=True)
print(state)


# GHZ-3 Algorithm

# Import relevant modules
from qiskit import *

# Create a Quantum Circuit acting on a quantum 3-qubit register
Q_circuit = QuantumCircuit(3)

# Add a H gate on qubit $q_{0}$, putting this qubit in superposition.
Q_circuit.h(0)

# Add a CX (CNOT) gate on control qubit $q_{0}$ and target qubit $q_{1}$, putting
# the qubits in a Bell state.
Q_circuit.cx(0, 1)

# Add a CX (CNOT) gate on control qubit $q_{0}$ and target qubit $q_{2}$, putting
# the qubits in a GHZ state.
Q_circuit.cx(0, 2)

# Draw the GHZ state circuit
Q_circuit.draw('mpl', filename="examples/GHZ-3/results/GHZ-3_Q-circuit")

# Import Aer
from qiskit import Aer

# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')

# Create a Quantum Program for execution
job = backend.run(Q_circuit)

result = job.result()
outputstate = result.get_statevector(Q_circuit, decimals=3)
print(outputstate)

from qiskit.visualization import plot_state_city
plot_state_city(outputstate, filename="examples/GHZ-3/results/GHZ-3_density")


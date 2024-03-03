#

# Import tools
from qiskit import QuantumCircuit
import os

# Input values
shots = 10000
result_path = "Lectures/#4/state_measurement/results/"
initial_state = [3./5., 4./5.]




#circuit = QuantumCircuit(2, 2)  # A circuit with 2 qubits and 2 classical bits
#circuit.measure(1, 0)           # Measures qubit 1 and puts the result in bit 0
#circuit.draw(filename=os.path.join(result_path, "ee1.png"))

circuit = QuantumCircuit(1)
circuit.measure_all() 
circuit.draw(filename=os.path.join(result_path, "ee1.png"))




#counts = result.get_counts(circuit)
#plot_histogram(counts, legend=None, color=['crimson'], title="Histogram", \
#    filename=os.path.join(result_path, "histogram_counts.png"))








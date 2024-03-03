# Representing qubit states

from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi


qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state = [0,1]   # Define initial_state as |1>
qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
#qc.draw()  # Let's view our circuit
# Draw the GHZ state circuit
qc.draw('mpl', filename="Q_simulation/intro1/results/figrr")


sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit
qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state = [0,1]   # Define initial_state as |1>
qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
qc.save_statevector()   # Tell simulator to save statevector
qobj = assemble(qc)     # Create a Qobj from the circuit for the simulator to run
result = sim.run(qobj).result() # Do the simulation and return the result

out_state = result.get_statevector()
print(out_state) # Display the output state vector


qc.measure_all()
qc.draw('mpl', filename="Q_simulation/intro1/results/measuree")
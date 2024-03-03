from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi, log2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def statevector_to_dict(sv):
    bit_mask = f"0{int(log2(len(sv)))}b"
    return {format(i, bit_mask): v.real for i, v in enumerate(sv)} 

def prep_folder(folder_path):
    if not os.path.exists(os.path.join(dir_path, folder_path)):
        os.makedirs(os.path.join(dir_path, folder_path), exist_ok=True)
    return os.path.join(dir_path, folder_path)

if __name__ == "__main__":
    Q_circuit = QuantumCircuit(1)  # Create a quantum circuit with one qubit
    initial_state = [0, 1]   # Define initial_state as |1>
    Q_circuit.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
    #Q_circuit.draw('mpl', filename="Lectures/#3/measurement/results/init_state")

    # Run the quantum circuit on a statevector simulator backend
    simulator = Aer.get_backend('statevector_simulator')

    # Create a Quantum Program for execution
    job = simulator.run(Q_circuit)
    result = job.result()
    outputstate = result.get_statevector(Q_circuit, decimals=3)
    print(outputstate)

    sv_dict = statevector_to_dict(outputstate.data)


    folder_path = prep_folder("images")
    file_name = "Qiskit_test_image"
    plot_histogram(sv_dict, legend=["legend"], color=['crimson'], title="New Histogram", filename=os.path.join(folder_path, file_name))


#----------------------------------------------------------------------------------
#

# Import tools
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

qc = QuantumCircuit(1) # Create a quantum circuit with one qubit

initial_state = [0,1]   # Define initial_state as |1>  ; = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>
qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
qc.draw()  # Let's view our circuit

sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit

qc.save_statevector()   # Tell simulator to save statevector
qobj = assemble(qc)     # Create a Qobj from the circuit for the simulator to run
result = sim.run(qobj).result() # Do the simulation and return the result


out_state = result.get_statevector()
print(out_state) # Display the output state vector

qc.measure_all()
qc.draw()

qobj = assemble(qc)
result = sim.run(qobj).result()
counts = result.get_counts()
plot_histogram(counts)





#S-----------



# Let's simulate our circuit in order to get the final state vector!
svsim = Aer.get_backend('statevector_simulator')

# Create a Qobj from the circuit for the simulator to run
qobj = assemble(qc)

# Do the simulation, return the result and get the state vector
result = svsim.run(qobj).result().get_statevector()

# Get the state vector for the first qubit
final_state = [result[0], result[1]]

print('a and b coefficients before simulation:', initial_state)
print('a and b coefficients after simulation:', final_state)




  

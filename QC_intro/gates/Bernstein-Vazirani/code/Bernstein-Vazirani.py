# Bernstein-Vazirani

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

Q_register = QuantumRegister(3, 'q')
anc = QuantumRegister(1, 'ancilla')
C_register = ClassicalRegister(3, 'c')
Q_circuit = QuantumCircuit(Q_register, anc, C_register)

Q_circuit.x(anc[0])
Q_circuit.h(anc[0])
Q_circuit.h(Q_register[0:3])
Q_circuit.cx(Q_register[0:3], anc[0])
Q_circuit.h(Q_register[0:3])
Q_circuit.barrier(Q_register)
Q_circuit.measure(Q_register, C_register)


# Draw the Bernstein-Vazirani circuit
Q_circuit.draw('mpl', filename="examples/Bernstein-Vazirani/results/Bernstein-Vazirani_Q-circuit")
print(C_register)
print(Q_register)

Q_circuit.draw('mpl')
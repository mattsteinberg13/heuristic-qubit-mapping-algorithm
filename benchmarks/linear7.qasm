version 1.0

qubits 7

h q[0]
h q[1]
x q[2]
y q[3]
z q[4]
h q[5]
y q[6]

cnot q[0],q[1]
cnot q[1],q[2]
cnot q[2],q[3]
cnot q[3],q[4]
cnot q[4],q[5]
cnot q[5],q[6]


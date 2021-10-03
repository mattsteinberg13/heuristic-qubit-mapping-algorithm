version 1.0 

qubits 4

x q[0]
x q[1]
s q[2]
h q[3]

cnot q[0],q[1]
cnot q[1],q[2]
cnot q[2],q[3]
cnot q[3],q[0]
cnot q[0],q[2]
cnot q[1],q[3]

x q[0]
x q[1]
s q[2]
h q[3]

cnot q[0],q[1]
cnot q[1],q[2]
cnot q[2],q[3]
cnot q[3],q[0]
cnot q[0],q[2]
cnot q[1],q[3]
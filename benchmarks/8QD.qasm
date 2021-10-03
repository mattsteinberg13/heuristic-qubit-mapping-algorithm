version 1.0 

qubits 8

x q[0]
x q[1]
s q[2]
h q[3]
z q[4]
y q[5]
h q[6]
h q[7]

cnot q[0],q[1]
cnot q[1],q[2]
cnot q[2],q[3]
cnot q[3],q[4]
cnot q[4],q[5]
cnot q[5],q[6]
cnot q[6],q[7]
cnot q[7],q[0]
cnot q[0],q[2]
cnot q[0],q[3]
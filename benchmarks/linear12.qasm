version 1.0

qubits 12

h q[0]
h q[1]
x q[2]
y q[3]
z q[4]
h q[5]
h q[6]
y q[7]
z q[8]
y q[9]
h q[10]
h q[11]

cnot q[2],q[3]
cnot q[4],q[5]
cnot q[1],q[2]
cnot q[3],q[4]
cnot q[5],q[6]
cnot q[0],q[1]
cnot q[2],q[3]
cnot q[4],q[5]
cnot q[6],q[7]
cnot q[1],q[2]
cnot q[3],q[4]
cnot q[5],q[6]
cnot q[2],q[3]
cnot q[4],q[5]
cnot q[7],q[8]
cnot q[8],q[9]
cnot q[9],q[10]
cnot q[10],q[11]
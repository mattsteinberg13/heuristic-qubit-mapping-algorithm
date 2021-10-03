version 1.0 

qubits 9

y q[2]
x q[1]
h q[3]
z q[0]
h q[5]
z q[4]
h q[6]
h q[7]
z q[8]

cnot q[0],q[1]
cnot q[1],q[2]
cnot q[2],q[3]
cnot q[3],q[4]
cnot q[4],q[5]
cnot q[5],q[6]
cnot q[6],q[7]
cnot q[7],q[8]


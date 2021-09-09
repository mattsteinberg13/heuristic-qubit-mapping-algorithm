import networkx as nx
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from networkx.algorithms import shortest_paths
import scipy
import itertools as iter
import operator
import os 
import re 

#reads cQASM files
def parser(filename):
    traffic = nx.Graph()
    #detect the path of the files to be used
    filepath = os.path.join("/home/matt7500/Dropbox/HQS/algorithms/benchmarks", filename)

    #search for this file in some directory 
    with open(filepath,"r") as cqasm: 
        #reads the qasm file
        lines = cqasm.readlines()

    #find the number of qubits for the algorithm
    for line in lines:  
        if line.startswith("qubits "):
            #need to find a way to save that line 
            number_qubits = int(line[7:len(line)-1])
            break
        elif not line.startswith("qubits "):
            continue
        else: 
            print("cQASM file has no quantum register.")
            return

    #initialize a complete graph with single and double weights and number_qubits amount of nodes
    # traffic = nx.complete_graph(number_qubits)
    for i in range(0,number_qubits):
        traffic.add_node(i,single=0)
    for j in range(0,number_qubits):
        for k in range(number_qubits-1,0,-1):
            if j != k:
                traffic.add_edge(j,k,double=0)
            elif j == k:
                continue 

    #list of single-qubit gates supported in cQASM
    list_s_gates = ["x","y","z","h","i","t","tdag","s","sdag","x90","y90","mx90","my90","rx","ry","rz"]
    #list of multiple-qubit gates supported in cQASM
    list_m_gates = ["cnot","toffoli","cz","swap","crk","cr"]
    #list of exceptions to be ignored
    list_exceptions = ["prep_x","prep_y","prep_z","measure_x","measure_y","measure","measure_all","measure_parity","c-x","c-z","version","#"]

    #search for single-qubit gates and add to NetworkX
    for j in range(0,len(list_s_gates)):
        for line in lines:
            if line.startswith(list_s_gates[j]):
                first_parenthesis = line.find("q[")
                second_parenthesis = line.find("]")
                number_single_gate = int(line[int(first_parenthesis)+2:int(second_parenthesis)])
                traffic.nodes[number_single_gate]["single"] = traffic.nodes[number_single_gate]["single"] + 1 
            else:
                continue 
    
    #first time - go through and create edges without weights for multi-qubit gates
    for k in range(0,len(list_m_gates)):
        for line in lines: 
            #for multiple-qubit gates
            if line.startswith(list_m_gates[k]):
                #cnot
                if list_m_gates[k] == "cnot":
                    # first_parenthesis = [int(s) for s in line.split() if s.isdigit()]
                    first_parenthesis = re.findall(r'\d+', line)
                    for z in range(0,len(first_parenthesis)):
                        first_parenthesis[z] = int(first_parenthesis[z])
                    # print(first_parenthesis)
                    number_multi_gate1 = first_parenthesis[0]
                    number_multi_gate2 = first_parenthesis[1]
                    #adds the commensurate edges to traffic graph 
                    traffic[number_multi_gate1][number_multi_gate2]["double"] = traffic[number_multi_gate1][number_multi_gate2]["double"] + 1

                #toffoli gate 
                elif list_m_gates[k] == "toffoli":
                    first_parenthesis = line.find("i q[")
                    number_multi_gate1 = int(line[int(first_parenthesis)+4])
                    number_multi_gate2 = int(line[int(first_parenthesis)+9])
                    number_multi_gate3 = int(line[int(first_parenthesis)+13])
                    #adds the commensurate edges to traffic graph 
                    traffic[number_multi_gate1][number_multi_gate2]["double"] = traffic[number_multi_gate1][number_multi_gate2]["double"] + 1
                    traffic[number_multi_gate2][number_multi_gate3]["double"] = traffic[number_multi_gate2][number_multi_gate3]["double"] + 1

                elif list_m_gates[k] == "cz":
                    first_parenthesis = line.find("z q[")
                    number_multi_gate1 = int(line[int(first_parenthesis)+4])
                    number_multi_gate2 = int(line[int(first_parenthesis)+9])
                    # print(traffic[number_multi_gate1][number_multi_gate2]["double"])
                    #adds the commensurate edges to traffic graph 
                    traffic[number_multi_gate1][number_multi_gate2]["double"] = traffic[number_multi_gate1][number_multi_gate2]["double"] + 1

                elif list_m_gates[k] == "swap":
                    first_parenthesis = line.find("p q[")
                    number_multi_gate1 = int(line[int(first_parenthesis)+4])
                    number_multi_gate2 = int(line[int(first_parenthesis)+9])
                    # print(traffic[number_multi_gate1][number_multi_gate2]["double"])
                    #adds the commensurate edges to traffic graph 
                    traffic[number_multi_gate1][number_multi_gate2]["double"] = traffic[number_multi_gate1][number_multi_gate2]["double"] + 1
                
                elif list_m_gates[k] == "crk":
                    first_parenthesis = line.find("k q[")
                    number_multi_gate1 = int(line[int(first_parenthesis)+4])
                    number_multi_gate2 = int(line[int(first_parenthesis)+9])
                    # print(traffic[number_multi_gate1][number_multi_gate2]["double"])
                    #adds the commensurate edges to traffic graph 
                    traffic[number_multi_gate1][number_multi_gate2]["double"] = traffic[number_multi_gate1][number_multi_gate2]["double"] + 1

                elif list_m_gates[k] == "cr":
                    first_parenthesis = line.find("r q[")
                    number_multi_gate1 = int(line[int(first_parenthesis)+4])
                    number_multi_gate2 = int(line[int(first_parenthesis)+9])
                    # print(traffic[number_multi_gate1][number_multi_gate2]["double"])
                    #adds the commensurate edges to traffic graph 
                    traffic[number_multi_gate1][number_multi_gate2]["double"] = traffic[number_multi_gate1][number_multi_gate2]["double"] + 1

                    # print(traffic.edges,traffic.nodes)
                #other gates
                else: 
                    continue 

    #find/delete all edges that have "double"=0
    double_0 = []
    for i in range(0,number_qubits):
        for j in range(number_qubits-1,-1,-1):
            if i != j: 
                if traffic[i][j]["double"] == 0:
                    double_0.append([i,j])
                elif traffic[i][j]["double"] != 0:
                    continue
                elif type(traffic[i][j]["double"]) != int:
                    print("error!!!!")
            elif i == j:
                continue

    # print("Before: ",len(double_0),double_0)
    # double_0 = double_0[0:(len(double_0)//2)]
    # print(len(double_0),double_0)

    double_0_new = {tuple(item) for item in map(sorted, double_0)}
    double_0_new = list(double_0_new)

    # print("After: ",len(double_0_new),double_0_new)

    for k in range(0,len(double_0_new)):
        if traffic[double_0_new[k][0]][double_0_new[k][1]]:
            traffic.remove_edge(double_0_new[k][0],double_0_new[k][1])
        else: 
            continue 
    # print(traffic.edges.data(),traffic.nodes.data(),double_0)
    return traffic 

#     nx.draw(traffic)
#     plt.draw()
#     plt.show()

# filename = "toffoli.qasm"
# parser(filename)
import networkx as nx
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from networkx.algorithms import shortest_paths
import time 
import itertools as iter
import operator
from parser import parser

###################################################################################################
#create QPU graph
def noise_graph():
    noise = nx.Graph()

    qpu_size = 3

    if qpu_size == 3:
        
        noise.add_node(0,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(1,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(2,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(3,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(4,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(5,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(6,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(7,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_node(8,weight=np.random.rand()/1000,read_out=np.random.rand()/100)
        noise.add_edge(0,1,weight=np.random.rand()/100)
        noise.add_edge(0,5,weight=np.random.rand()/100)
        noise.add_edge(1,2,weight=np.random.rand()/100)
        noise.add_edge(1,4,weight=np.random.rand()/100)
        noise.add_edge(2,3,weight=np.random.rand()/100)
        noise.add_edge(3,4,weight=np.random.rand()/100)
        noise.add_edge(3,8,weight=np.random.rand()/100)
        noise.add_edge(4,5,weight=np.random.rand()/100)
        noise.add_edge(4,7,weight=np.random.rand()/100)
        noise.add_edge(5,6,weight=np.random.rand()/100)
        noise.add_edge(6,7,weight=np.random.rand()/100)
        noise.add_edge(7,8,weight=np.random.rand()/100)

    elif qpu_size == 4:
        
        noise.add_node(0,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(1,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(2,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(3,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(4,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(5,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(6,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(7,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(8,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(9,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(10,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(11,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(12,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(13,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(14,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(15,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_edge(0,1,weight=4*np.random.rand()/100)
        noise.add_edge(0,7,weight=4*np.random.rand()/100)
        noise.add_edge(1,2,weight=4*np.random.rand()/100)
        noise.add_edge(1,6,weight=4*np.random.rand()/100)
        noise.add_edge(2,5,weight=4*np.random.rand()/100)
        noise.add_edge(3,2,weight=4*np.random.rand()/100)
        noise.add_edge(3,4,weight=4*np.random.rand()/100)
        noise.add_edge(4,5,weight=4*np.random.rand()/100)
        noise.add_edge(4,11,weight=4*np.random.rand()/100)
        noise.add_edge(5,8,weight=4*np.random.rand()/100)
        noise.add_edge(6,5,weight=4*np.random.rand()/100)
        noise.add_edge(5,10,weight=4*np.random.rand()/100)
        noise.add_edge(6,9,weight=4*np.random.rand()/100)
        noise.add_edge(6,7,weight=4*np.random.rand()/100)
        noise.add_edge(8,7,weight=4*np.random.rand()/100)
        noise.add_edge(8,15,weight=4*np.random.rand()/100)
        noise.add_edge(8,9,weight=4*np.random.rand()/100)
        noise.add_edge(9,10,weight=4*np.random.rand()/100)
        noise.add_edge(9,14,weight=4*np.random.rand()/100)
        noise.add_edge(10,13,weight=4*np.random.rand()/100)
        noise.add_edge(11,10,weight=4*np.random.rand()/100)
        noise.add_edge(11,12,weight=4*np.random.rand()/100)
        noise.add_edge(12,13,weight=4*np.random.rand()/100)
        noise.add_edge(13,14,weight=4*np.random.rand()/100)
        noise.add_edge(14,15,weight=4*np.random.rand()/100)

    elif qpu_size == 5:
         
        noise.add_node(0,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(1,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(2,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(3,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(4,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(5,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(6,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(7,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(8,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(9,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(10,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(11,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(12,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(13,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(14,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(15,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(16,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(17,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(18,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(19,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(20,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(21,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(22,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(23,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(24,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_edge(0,1,weight=4*np.random.rand()/100)
        noise.add_edge(0,9,weight=4*np.random.rand()/100)
        noise.add_edge(1,2,weight=4*np.random.rand()/100)
        noise.add_edge(1,8,weight=4*np.random.rand()/100)
        noise.add_edge(2,3,weight=4*np.random.rand()/100)
        noise.add_edge(2,7,weight=4*np.random.rand()/100)
        noise.add_edge(3,6,weight=4*np.random.rand()/100)
        noise.add_edge(3,4,weight=4*np.random.rand()/100)
        noise.add_edge(4,5,weight=4*np.random.rand()/100)
        noise.add_edge(5,14,weight=4*np.random.rand()/100)
        noise.add_edge(5,6,weight=4*np.random.rand()/100)
        noise.add_edge(6,13,weight=4*np.random.rand()/100)
        noise.add_edge(6,7,weight=4*np.random.rand()/100)
        noise.add_edge(7,12,weight=4*np.random.rand()/100)
        noise.add_edge(7,8,weight=4*np.random.rand()/100)
        noise.add_edge(8,11,weight=4*np.random.rand()/100)
        noise.add_edge(8,9,weight=4*np.random.rand()/100)
        noise.add_edge(9,10,weight=4*np.random.rand()/100)
        noise.add_edge(10,19,weight=4*np.random.rand()/100)
        noise.add_edge(10,11,weight=4*np.random.rand()/100)
        noise.add_edge(11,18,weight=4*np.random.rand()/100)
        noise.add_edge(12,11,weight=4*np.random.rand()/100)
        noise.add_edge(12,17,weight=4*np.random.rand()/100)
        noise.add_edge(12,13,weight=4*np.random.rand()/100)
        noise.add_edge(13,16,weight=4*np.random.rand()/100)
        noise.add_edge(13,14,weight=4*np.random.rand()/100)
        noise.add_edge(14,15,weight=4*np.random.rand()/100)
        noise.add_edge(15,24,weight=4*np.random.rand()/100)
        noise.add_edge(15,16,weight=4*np.random.rand()/100)
        noise.add_edge(16,23,weight=4*np.random.rand()/100)
        noise.add_edge(16,17,weight=4*np.random.rand()/100)
        noise.add_edge(17,18,weight=4*np.random.rand()/100)
        noise.add_edge(17,22,weight=4*np.random.rand()/100)
        noise.add_edge(18,21,weight=4*np.random.rand()/100)
        noise.add_edge(18,19,weight=4*np.random.rand()/100)
        noise.add_edge(20,19,weight=4*np.random.rand()/100)
        noise.add_edge(20,21,weight=4*np.random.rand()/100)
        noise.add_edge(22,21,weight=4*np.random.rand()/100)
        noise.add_edge(22,23,weight=4*np.random.rand()/100)
        noise.add_edge(24,23,weight=4*np.random.rand()/100)

    elif qpu_size == 6:

        noise.add_node(0,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(1,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(2,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(3,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(4,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(5,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(6,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(7,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(8,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(9,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(10,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(11,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(12,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(13,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(14,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(15,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(16,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(17,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(18,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(19,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(20,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(21,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(22,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(23,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(24,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(25,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(26,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(27,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(28,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(29,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(30,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(31,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(32,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(33,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(34,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(35,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_edge(0,1,weight=4*np.random.rand()/100)
        noise.add_edge(0,11,weight=4*np.random.rand()/100)
        noise.add_edge(2,1,weight=4*np.random.rand()/100)
        noise.add_edge(10,1,weight=4*np.random.rand()/100)
        noise.add_edge(2,3,weight=4*np.random.rand()/100)
        noise.add_edge(2,9,weight=4*np.random.rand()/100)
        noise.add_edge(3,8,weight=4*np.random.rand()/100)
        noise.add_edge(3,4,weight=4*np.random.rand()/100)
        noise.add_edge(4,5,weight=4*np.random.rand()/100)
        noise.add_edge(4,7,weight=4*np.random.rand()/100)
        noise.add_edge(5,6,weight=4*np.random.rand()/100)
        noise.add_edge(6,17,weight=4*np.random.rand()/100)
        noise.add_edge(6,7,weight=4*np.random.rand()/100)
        noise.add_edge(7,16,weight=4*np.random.rand()/100)
        noise.add_edge(7,8,weight=4*np.random.rand()/100)
        noise.add_edge(8,15,weight=4*np.random.rand()/100)
        noise.add_edge(8,9,weight=4*np.random.rand()/100)
        noise.add_edge(9,10,weight=4*np.random.rand()/100)
        noise.add_edge(9,14,weight=4*np.random.rand()/100)
        noise.add_edge(10,11,weight=4*np.random.rand()/100)
        noise.add_edge(10,13,weight=4*np.random.rand()/100)
        noise.add_edge(12,11,weight=4*np.random.rand()/100)
        noise.add_edge(12,23,weight=4*np.random.rand()/100)
        noise.add_edge(12,13,weight=4*np.random.rand()/100)
        noise.add_edge(13,22,weight=4*np.random.rand()/100)
        noise.add_edge(13,14,weight=4*np.random.rand()/100)
        noise.add_edge(14,15,weight=4*np.random.rand()/100)
        noise.add_edge(14,21,weight=4*np.random.rand()/100)
        noise.add_edge(20,15,weight=4*np.random.rand()/100)
        noise.add_edge(15,16,weight=4*np.random.rand()/100)
        noise.add_edge(16,19,weight=4*np.random.rand()/100)
        noise.add_edge(17,16,weight=4*np.random.rand()/100)
        noise.add_edge(17,18,weight=4*np.random.rand()/100)
        noise.add_edge(19,18,weight=4*np.random.rand()/100)
        noise.add_edge(29,18,weight=4*np.random.rand()/100)
        noise.add_edge(20,19,weight=4*np.random.rand()/100)
        noise.add_edge(28,19,weight=4*np.random.rand()/100)
        noise.add_edge(20,21,weight=4*np.random.rand()/100)
        noise.add_edge(20,27,weight=4*np.random.rand()/100)
        noise.add_edge(21,26,weight=4*np.random.rand()/100)
        noise.add_edge(21,22,weight=4*np.random.rand()/100)
        noise.add_edge(22,25,weight=4*np.random.rand()/100)
        noise.add_edge(22,23,weight=4*np.random.rand()/100)
        noise.add_edge(23,24,weight=4*np.random.rand()/100)
        noise.add_edge(24,35,weight=4*np.random.rand()/100)
        noise.add_edge(24,25,weight=4*np.random.rand()/100)
        noise.add_edge(25,34,weight=4*np.random.rand()/100)
        noise.add_edge(25,26,weight=4*np.random.rand()/100)
        noise.add_edge(26,33,weight=4*np.random.rand()/100)
        noise.add_edge(27,26,weight=4*np.random.rand()/100)
        noise.add_edge(27,32,weight=4*np.random.rand()/100)
        noise.add_edge(27,28,weight=4*np.random.rand()/100)
        noise.add_edge(28,31,weight=4*np.random.rand()/100)
        noise.add_edge(28,29,weight=4*np.random.rand()/100)
        noise.add_edge(29,30,weight=4*np.random.rand()/100)
        noise.add_edge(30,31,weight=4*np.random.rand()/100)
        noise.add_edge(32,31,weight=4*np.random.rand()/100)
        noise.add_edge(33,32,weight=4*np.random.rand()/100)
        noise.add_edge(34,33,weight=4*np.random.rand()/100)
        noise.add_edge(34,35,weight=4*np.random.rand()/100)

    elif qpu_size == 7:

        noise.add_node(0,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(1,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(2,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(3,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(4,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(5,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(6,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(7,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(8,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(9,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(10,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(11,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(12,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(13,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(14,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(15,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(16,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(17,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(18,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(19,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(20,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(21,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(22,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(23,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(24,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(25,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(26,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(27,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(28,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(29,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(30,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(31,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(32,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(33,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(34,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(35,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(36,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(37,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(38,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(39,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(40,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(41,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(42,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(43,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(44,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(45,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(46,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(47,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(48,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_edge(0,1,weight=4*np.random.rand()/100)
        noise.add_edge(0,13,weight=4*np.random.rand()/100)
        noise.add_edge(2,1,weight=4*np.random.rand()/100)
        noise.add_edge(12,1,weight=4*np.random.rand()/100)
        noise.add_edge(2,3,weight=4*np.random.rand()/100)
        noise.add_edge(2,11,weight=4*np.random.rand()/100)
        noise.add_edge(3,10,weight=4*np.random.rand()/100)
        noise.add_edge(3,4,weight=4*np.random.rand()/100)
        noise.add_edge(4,9,weight=4*np.random.rand()/100)
        noise.add_edge(5,4,weight=4*np.random.rand()/100)
        noise.add_edge(5,8,weight=4*np.random.rand()/100)
        noise.add_edge(6,5,weight=4*np.random.rand()/100)
        noise.add_edge(6,7,weight=4*np.random.rand()/100)
        noise.add_edge(7,20,weight=4*np.random.rand()/100)
        noise.add_edge(7,8,weight=4*np.random.rand()/100)
        noise.add_edge(8,19,weight=4*np.random.rand()/100)
        noise.add_edge(8,9,weight=4*np.random.rand()/100)
        noise.add_edge(9,18,weight=4*np.random.rand()/100)
        noise.add_edge(9,10,weight=4*np.random.rand()/100)
        noise.add_edge(10,11,weight=4*np.random.rand()/100)
        noise.add_edge(10,17,weight=4*np.random.rand()/100)
        noise.add_edge(16,11,weight=4*np.random.rand()/100)
        noise.add_edge(12,11,weight=4*np.random.rand()/100)
        noise.add_edge(12,15,weight=4*np.random.rand()/100)
        noise.add_edge(13,12,weight=4*np.random.rand()/100)
        noise.add_edge(13,14,weight=4*np.random.rand()/100)
        noise.add_edge(14,27,weight=4*np.random.rand()/100)
        noise.add_edge(14,15,weight=4*np.random.rand()/100)
        noise.add_edge(15,26,weight=4*np.random.rand()/100)
        noise.add_edge(16,15,weight=4*np.random.rand()/100)
        noise.add_edge(16,25,weight=4*np.random.rand()/100)
        noise.add_edge(17,16,weight=4*np.random.rand()/100)
        noise.add_edge(24,17,weight=4*np.random.rand()/100)
        noise.add_edge(17,18,weight=4*np.random.rand()/100)
        noise.add_edge(23,18,weight=4*np.random.rand()/100)
        noise.add_edge(18,19,weight=4*np.random.rand()/100)
        noise.add_edge(22,19,weight=4*np.random.rand()/100)
        noise.add_edge(19,20,weight=4*np.random.rand()/100)
        noise.add_edge(20,21,weight=4*np.random.rand()/100)
        noise.add_edge(21,34,weight=4*np.random.rand()/100)
        noise.add_edge(22,21,weight=4*np.random.rand()/100)
        noise.add_edge(22,33,weight=4*np.random.rand()/100)
        noise.add_edge(23,22,weight=4*np.random.rand()/100)
        noise.add_edge(23,32,weight=4*np.random.rand()/100)
        noise.add_edge(23,24,weight=4*np.random.rand()/100)
        noise.add_edge(31,24,weight=4*np.random.rand()/100)
        noise.add_edge(25,24,weight=4*np.random.rand()/100)
        noise.add_edge(25,30,weight=4*np.random.rand()/100)
        noise.add_edge(26,29,weight=4*np.random.rand()/100)
        noise.add_edge(26,27,weight=4*np.random.rand()/100)
        noise.add_edge(27,28,weight=4*np.random.rand()/100)
        noise.add_edge(28,41,weight=4*np.random.rand()/100)
        noise.add_edge(28,29,weight=4*np.random.rand()/100)
        noise.add_edge(29,40,weight=4*np.random.rand()/100)
        noise.add_edge(29,30,weight=4*np.random.rand()/100)
        noise.add_edge(30,39,weight=4*np.random.rand()/100)
        noise.add_edge(30,31,weight=4*np.random.rand()/100)
        noise.add_edge(38,31,weight=4*np.random.rand()/100)
        noise.add_edge(31,32,weight=4*np.random.rand()/100)
        noise.add_edge(32,37,weight=4*np.random.rand()/100)
        noise.add_edge(32,33,weight=4*np.random.rand()/100)
        noise.add_edge(36,33,weight=4*np.random.rand()/100)
        noise.add_edge(34,33,weight=4*np.random.rand()/100)
        noise.add_edge(34,35,weight=4*np.random.rand()/100)
        noise.add_edge(35,48,weight=4*np.random.rand()/100)
        noise.add_edge(35,36,weight=4*np.random.rand()/100)
        noise.add_edge(36,47,weight=4*np.random.rand()/100)
        noise.add_edge(36,37,weight=4*np.random.rand()/100)
        noise.add_edge(37,46,weight=4*np.random.rand()/100)
        noise.add_edge(38,37,weight=4*np.random.rand()/100)
        noise.add_edge(38,45,weight=4*np.random.rand()/100)
        noise.add_edge(38,39,weight=4*np.random.rand()/100)
        noise.add_edge(39,44,weight=4*np.random.rand()/100)
        noise.add_edge(39,40,weight=4*np.random.rand()/100)
        noise.add_edge(40,43,weight=4*np.random.rand()/100)
        noise.add_edge(40,41,weight=4*np.random.rand()/100)
        noise.add_edge(41,42,weight=4*np.random.rand()/100)
        noise.add_edge(42,43,weight=4*np.random.rand()/100)
        noise.add_edge(43,44,weight=4*np.random.rand()/100)
        noise.add_edge(44,45,weight=4*np.random.rand()/100)
        noise.add_edge(45,46,weight=4*np.random.rand()/100)
        noise.add_edge(46,47,weight=4*np.random.rand()/100)
        noise.add_edge(47,48,weight=4*np.random.rand()/100)

    elif qpu_size == 8:

        noise.add_node(0,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(1,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(2,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(3,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(4,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(5,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(6,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(7,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(8,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(9,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(10,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(11,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(12,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(13,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(14,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(15,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(16,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(17,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(18,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(19,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(20,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(21,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(22,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(23,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(24,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(25,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(26,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(27,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(28,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(29,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(30,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(31,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(32,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(33,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(34,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(35,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(36,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(37,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(38,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(39,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(40,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(41,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(42,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(43,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(44,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(45,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(46,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(47,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(48,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(49,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(50,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(51,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(52,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(53,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(54,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(55,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(56,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(57,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(58,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(59,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(60,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(61,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(62,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_node(63,weight=4*np.random.rand()/1000,read_out=4*np.random.rand()/100)
        noise.add_edge(0,1,weight=4*np.random.rand()/100)
        noise.add_edge(0,13,weight=4*np.random.rand()/100)
        noise.add_edge(2,1,weight=4*np.random.rand()/100)
        noise.add_edge(12,1,weight=4*np.random.rand()/100)
        noise.add_edge(2,3,weight=4*np.random.rand()/100)
        noise.add_edge(2,11,weight=4*np.random.rand()/100)
        noise.add_edge(3,10,weight=4*np.random.rand()/100)
        noise.add_edge(3,4,weight=4*np.random.rand()/100)
        noise.add_edge(4,9,weight=4*np.random.rand()/100)
        noise.add_edge(5,4,weight=4*np.random.rand()/100)
        noise.add_edge(5,8,weight=4*np.random.rand()/100)
        noise.add_edge(6,5,weight=4*np.random.rand()/100)
        noise.add_edge(6,7,weight=4*np.random.rand()/100)
        noise.add_edge(7,20,weight=4*np.random.rand()/100)
        noise.add_edge(7,8,weight=4*np.random.rand()/100)
        noise.add_edge(8,19,weight=4*np.random.rand()/100)
        noise.add_edge(8,9,weight=4*np.random.rand()/100)
        noise.add_edge(9,18,weight=4*np.random.rand()/100)
        noise.add_edge(9,10,weight=4*np.random.rand()/100)
        noise.add_edge(10,11,weight=4*np.random.rand()/100)
        noise.add_edge(10,17,weight=4*np.random.rand()/100)
        noise.add_edge(16,11,weight=4*np.random.rand()/100)
        noise.add_edge(12,11,weight=4*np.random.rand()/100)
        noise.add_edge(12,15,weight=4*np.random.rand()/100)
        noise.add_edge(13,12,weight=4*np.random.rand()/100)
        noise.add_edge(13,14,weight=4*np.random.rand()/100)
        noise.add_edge(14,27,weight=4*np.random.rand()/100)
        noise.add_edge(14,15,weight=4*np.random.rand()/100)
        noise.add_edge(15,26,weight=4*np.random.rand()/100)
        noise.add_edge(16,15,weight=4*np.random.rand()/100)
        noise.add_edge(16,25,weight=4*np.random.rand()/100)
        noise.add_edge(17,16,weight=4*np.random.rand()/100)
        noise.add_edge(24,17,weight=4*np.random.rand()/100)
        noise.add_edge(17,18,weight=4*np.random.rand()/100)
        noise.add_edge(23,18,weight=4*np.random.rand()/100)
        noise.add_edge(18,19,weight=4*np.random.rand()/100)
        noise.add_edge(22,19,weight=4*np.random.rand()/100)
        noise.add_edge(19,20,weight=4*np.random.rand()/100)
        noise.add_edge(20,21,weight=4*np.random.rand()/100)
        noise.add_edge(21,34,weight=4*np.random.rand()/100)
        noise.add_edge(22,21,weight=4*np.random.rand()/100)
        noise.add_edge(22,33,weight=4*np.random.rand()/100)
        noise.add_edge(23,22,weight=4*np.random.rand()/100)
        noise.add_edge(23,32,weight=4*np.random.rand()/100)
        noise.add_edge(23,24,weight=4*np.random.rand()/100)
        noise.add_edge(31,24,weight=4*np.random.rand()/100)
        noise.add_edge(25,24,weight=4*np.random.rand()/100)
        noise.add_edge(25,30,weight=4*np.random.rand()/100)
        noise.add_edge(26,29,weight=4*np.random.rand()/100)
        noise.add_edge(26,27,weight=4*np.random.rand()/100)
        noise.add_edge(27,28,weight=4*np.random.rand()/100)
        noise.add_edge(28,41,weight=4*np.random.rand()/100)
        noise.add_edge(28,29,weight=4*np.random.rand()/100)
        noise.add_edge(29,40,weight=4*np.random.rand()/100)
        noise.add_edge(29,30,weight=4*np.random.rand()/100)
        noise.add_edge(30,39,weight=4*np.random.rand()/100)
        noise.add_edge(30,31,weight=4*np.random.rand()/100)
        noise.add_edge(38,31,weight=4*np.random.rand()/100)
        noise.add_edge(31,32,weight=4*np.random.rand()/100)
        noise.add_edge(32,37,weight=4*np.random.rand()/100)
        noise.add_edge(32,33,weight=4*np.random.rand()/100)
        noise.add_edge(36,33,weight=4*np.random.rand()/100)
        noise.add_edge(34,33,weight=4*np.random.rand()/100)
        noise.add_edge(34,35,weight=4*np.random.rand()/100)
        noise.add_edge(35,48,weight=4*np.random.rand()/100)
        noise.add_edge(35,36,weight=4*np.random.rand()/100)
        noise.add_edge(36,47,weight=4*np.random.rand()/100)
        noise.add_edge(36,37,weight=4*np.random.rand()/100)
        noise.add_edge(37,46,weight=4*np.random.rand()/100)
        noise.add_edge(38,37,weight=4*np.random.rand()/100)
        noise.add_edge(38,45,weight=4*np.random.rand()/100)
        noise.add_edge(38,39,weight=4*np.random.rand()/100)
        noise.add_edge(39,44,weight=4*np.random.rand()/100)
        noise.add_edge(39,40,weight=4*np.random.rand()/100)
        noise.add_edge(40,43,weight=4*np.random.rand()/100)
        noise.add_edge(40,41,weight=4*np.random.rand()/100)
        noise.add_edge(41,42,weight=4*np.random.rand()/100)
        noise.add_edge(42,43,weight=4*np.random.rand()/100)
        noise.add_edge(43,44,weight=4*np.random.rand()/100)
        noise.add_edge(44,45,weight=4*np.random.rand()/100)
        noise.add_edge(45,46,weight=4*np.random.rand()/100)
        noise.add_edge(46,47,weight=4*np.random.rand()/100)
        noise.add_edge(47,48,weight=4*np.random.rand()/100)
        noise.add_edge(49,48,weight=4*np.random.rand()/100)
        noise.add_edge(49,50,weight=4*np.random.rand()/100)
        noise.add_edge(47,50,weight=4*np.random.rand()/100)
        noise.add_edge(51,50,weight=4*np.random.rand()/100)
        noise.add_edge(46,51,weight=4*np.random.rand()/100)
        noise.add_edge(51,52,weight=4*np.random.rand()/100)
        noise.add_edge(52,45,weight=4*np.random.rand()/100)
        noise.add_edge(52,53,weight=4*np.random.rand()/100)
        noise.add_edge(44,53,weight=4*np.random.rand()/100)
        noise.add_edge(53,54,weight=4*np.random.rand()/100)
        noise.add_edge(43,54,weight=4*np.random.rand()/100)
        noise.add_edge(54,55,weight=4*np.random.rand()/100)
        noise.add_edge(42,55,weight=4*np.random.rand()/100)
        noise.add_edge(55,56,weight=4*np.random.rand()/100)
        noise.add_edge(57,56,weight=4*np.random.rand()/100)
        noise.add_edge(42,57,weight=4*np.random.rand()/100)
        noise.add_edge(41,58,weight=4*np.random.rand()/100)
        noise.add_edge(57,58,weight=4*np.random.rand()/100)
        noise.add_edge(58,59,weight=4*np.random.rand()/100)
        noise.add_edge(28,59,weight=4*np.random.rand()/100)
        noise.add_edge(60,59,weight=4*np.random.rand()/100)
        noise.add_edge(60,27,weight=4*np.random.rand()/100)
        noise.add_edge(61,60,weight=4*np.random.rand()/100)
        noise.add_edge(61,14,weight=4*np.random.rand()/100)
        noise.add_edge(62,61,weight=4*np.random.rand()/100)
        noise.add_edge(62,13,weight=4*np.random.rand()/100)
        noise.add_edge(62,63,weight=4*np.random.rand()/100)
        noise.add_edge(0,63,weight=4*np.random.rand()/100)

    elif qpu_size == 9:

        noise.add_node(0,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(1,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(2,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(3,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(4,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(5,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(6,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(7,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(8,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(9,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(10,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(11,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(12,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(13,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(14,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(15,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(16,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(17,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(18,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(19,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(20,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(21,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(22,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(23,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(24,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(25,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(26,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(27,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(28,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(29,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(30,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(31,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(32,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(33,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(34,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(35,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(36,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(37,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(38,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(39,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(40,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(41,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(42,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(43,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(44,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(45,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(46,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(47,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(48,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(49,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(50,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(51,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(52,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(53,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(54,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(55,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(56,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(57,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(58,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(59,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(60,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(61,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(62,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(63,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(64,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(65,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(66,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(67,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(68,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(69,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(70,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(71,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(72,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(73,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(74,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(75,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(76,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(77,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(78,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(79,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_node(80,weight=64*np.random.rand()/1000,read_out=64*np.random.rand()/100)
        noise.add_edge(0,1,weight=64*np.random.rand()/100)
        noise.add_edge(0,13,weight=64*np.random.rand()/100)
        noise.add_edge(2,1,weight=64*np.random.rand()/100)
        noise.add_edge(12,1,weight=64*np.random.rand()/100)
        noise.add_edge(2,3,weight=64*np.random.rand()/100)
        noise.add_edge(2,11,weight=64*np.random.rand()/100)
        noise.add_edge(3,10,weight=64*np.random.rand()/100)
        noise.add_edge(3,4,weight=64*np.random.rand()/100)
        noise.add_edge(4,9,weight=64*np.random.rand()/100)
        noise.add_edge(5,4,weight=64*np.random.rand()/100)
        noise.add_edge(5,8,weight=64*np.random.rand()/100)
        noise.add_edge(6,5,weight=64*np.random.rand()/100)
        noise.add_edge(6,7,weight=64*np.random.rand()/100)
        noise.add_edge(7,20,weight=64*np.random.rand()/100)
        noise.add_edge(7,8,weight=64*np.random.rand()/100)
        noise.add_edge(8,19,weight=64*np.random.rand()/100)
        noise.add_edge(8,9,weight=64*np.random.rand()/100)
        noise.add_edge(9,18,weight=64*np.random.rand()/100)
        noise.add_edge(9,10,weight=64*np.random.rand()/100)
        noise.add_edge(10,11,weight=64*np.random.rand()/100)
        noise.add_edge(10,17,weight=64*np.random.rand()/100)
        noise.add_edge(16,11,weight=64*np.random.rand()/100)
        noise.add_edge(12,11,weight=64*np.random.rand()/100)
        noise.add_edge(12,15,weight=64*np.random.rand()/100)
        noise.add_edge(13,12,weight=64*np.random.rand()/100)
        noise.add_edge(13,14,weight=64*np.random.rand()/100)
        noise.add_edge(14,27,weight=64*np.random.rand()/100)
        noise.add_edge(14,15,weight=64*np.random.rand()/100)
        noise.add_edge(15,26,weight=64*np.random.rand()/100)
        noise.add_edge(16,15,weight=64*np.random.rand()/100)
        noise.add_edge(16,25,weight=64*np.random.rand()/100)
        noise.add_edge(17,16,weight=64*np.random.rand()/100)
        noise.add_edge(24,17,weight=64*np.random.rand()/100)
        noise.add_edge(17,18,weight=64*np.random.rand()/100)
        noise.add_edge(23,18,weight=64*np.random.rand()/100)
        noise.add_edge(18,19,weight=64*np.random.rand()/100)
        noise.add_edge(22,19,weight=64*np.random.rand()/100)
        noise.add_edge(19,20,weight=64*np.random.rand()/100)
        noise.add_edge(20,21,weight=64*np.random.rand()/100)
        noise.add_edge(21,34,weight=64*np.random.rand()/100)
        noise.add_edge(22,21,weight=64*np.random.rand()/100)
        noise.add_edge(22,33,weight=64*np.random.rand()/100)
        noise.add_edge(23,22,weight=64*np.random.rand()/100)
        noise.add_edge(23,32,weight=64*np.random.rand()/100)
        noise.add_edge(23,24,weight=64*np.random.rand()/100)
        noise.add_edge(31,24,weight=64*np.random.rand()/100)
        noise.add_edge(25,24,weight=64*np.random.rand()/100)
        noise.add_edge(25,30,weight=64*np.random.rand()/100)
        noise.add_edge(26,29,weight=64*np.random.rand()/100)
        noise.add_edge(26,27,weight=64*np.random.rand()/100)
        noise.add_edge(27,28,weight=64*np.random.rand()/100)
        noise.add_edge(28,41,weight=64*np.random.rand()/100)
        noise.add_edge(28,29,weight=64*np.random.rand()/100)
        noise.add_edge(29,40,weight=64*np.random.rand()/100)
        noise.add_edge(29,30,weight=64*np.random.rand()/100)
        noise.add_edge(30,39,weight=64*np.random.rand()/100)
        noise.add_edge(30,31,weight=64*np.random.rand()/100)
        noise.add_edge(38,31,weight=64*np.random.rand()/100)
        noise.add_edge(31,32,weight=64*np.random.rand()/100)
        noise.add_edge(32,37,weight=64*np.random.rand()/100)
        noise.add_edge(32,33,weight=64*np.random.rand()/100)
        noise.add_edge(36,33,weight=64*np.random.rand()/100)
        noise.add_edge(34,33,weight=64*np.random.rand()/100)
        noise.add_edge(34,35,weight=64*np.random.rand()/100)
        noise.add_edge(35,48,weight=64*np.random.rand()/100)
        noise.add_edge(35,36,weight=64*np.random.rand()/100)
        noise.add_edge(36,47,weight=64*np.random.rand()/100)
        noise.add_edge(36,37,weight=64*np.random.rand()/100)
        noise.add_edge(37,46,weight=64*np.random.rand()/100)
        noise.add_edge(38,37,weight=64*np.random.rand()/100)
        noise.add_edge(38,45,weight=64*np.random.rand()/100)
        noise.add_edge(38,39,weight=64*np.random.rand()/100)
        noise.add_edge(39,44,weight=64*np.random.rand()/100)
        noise.add_edge(39,40,weight=64*np.random.rand()/100)
        noise.add_edge(40,43,weight=64*np.random.rand()/100)
        noise.add_edge(40,41,weight=64*np.random.rand()/100)
        noise.add_edge(41,42,weight=64*np.random.rand()/100)
        noise.add_edge(42,43,weight=64*np.random.rand()/100)
        noise.add_edge(43,44,weight=64*np.random.rand()/100)
        noise.add_edge(44,45,weight=64*np.random.rand()/100)
        noise.add_edge(45,46,weight=64*np.random.rand()/100)
        noise.add_edge(46,47,weight=64*np.random.rand()/100)
        noise.add_edge(47,48,weight=64*np.random.rand()/100)
        noise.add_edge(49,48,weight=64*np.random.rand()/100)
        noise.add_edge(49,50,weight=64*np.random.rand()/100)
        noise.add_edge(47,50,weight=64*np.random.rand()/100)
        noise.add_edge(51,50,weight=64*np.random.rand()/100)
        noise.add_edge(46,51,weight=64*np.random.rand()/100)
        noise.add_edge(51,52,weight=64*np.random.rand()/100)
        noise.add_edge(52,45,weight=64*np.random.rand()/100)
        noise.add_edge(52,53,weight=64*np.random.rand()/100)
        noise.add_edge(44,53,weight=64*np.random.rand()/100)
        noise.add_edge(53,54,weight=64*np.random.rand()/100)
        noise.add_edge(43,54,weight=64*np.random.rand()/100)
        noise.add_edge(54,55,weight=64*np.random.rand()/100)
        noise.add_edge(42,55,weight=64*np.random.rand()/100)
        noise.add_edge(55,56,weight=64*np.random.rand()/100)
        noise.add_edge(57,56,weight=64*np.random.rand()/100)
        noise.add_edge(42,57,weight=64*np.random.rand()/100)
        noise.add_edge(41,58,weight=64*np.random.rand()/100)
        noise.add_edge(57,58,weight=64*np.random.rand()/100)
        noise.add_edge(58,59,weight=64*np.random.rand()/100)
        noise.add_edge(28,59,weight=64*np.random.rand()/100)
        noise.add_edge(60,59,weight=64*np.random.rand()/100)
        noise.add_edge(60,27,weight=64*np.random.rand()/100)
        noise.add_edge(61,60,weight=64*np.random.rand()/100)
        noise.add_edge(61,14,weight=64*np.random.rand()/100)
        noise.add_edge(62,61,weight=64*np.random.rand()/100)
        noise.add_edge(62,13,weight=64*np.random.rand()/100)
        noise.add_edge(62,63,weight=64*np.random.rand()/100)
        noise.add_edge(0,63,weight=64*np.random.rand()/100)
        noise.add_edge(64,63,weight=64*np.random.rand()/100)
        noise.add_edge(65,64,weight=64*np.random.rand()/100)
        noise.add_edge(62,65,weight=64*np.random.rand()/100)
        noise.add_edge(65,66,weight=64*np.random.rand()/100)
        noise.add_edge(61,66,weight=64*np.random.rand()/100)
        noise.add_edge(66,67,weight=64*np.random.rand()/100)
        noise.add_edge(60,67,weight=64*np.random.rand()/100)
        noise.add_edge(0,63,weight=64*np.random.rand()/100)
        noise.add_edge(67,68,weight=64*np.random.rand()/100)
        noise.add_edge(59,68,weight=64*np.random.rand()/100)
        noise.add_edge(68,69,weight=64*np.random.rand()/100)
        noise.add_edge(58,69,weight=64*np.random.rand()/100)
        noise.add_edge(69,70,weight=64*np.random.rand()/100)
        noise.add_edge(57,70,weight=64*np.random.rand()/100)
        noise.add_edge(71,70,weight=64*np.random.rand()/100)
        noise.add_edge(71,72,weight=64*np.random.rand()/100)
        noise.add_edge(71,56,weight=64*np.random.rand()/100)
        noise.add_edge(72,73,weight=64*np.random.rand()/100)
        noise.add_edge(56,73,weight=64*np.random.rand()/100)
        noise.add_edge(73,74,weight=64*np.random.rand()/100)
        noise.add_edge(55,74,weight=64*np.random.rand()/100)
        noise.add_edge(75,74,weight=64*np.random.rand()/100)
        noise.add_edge(75,54,weight=64*np.random.rand()/100)
        noise.add_edge(75,76,weight=64*np.random.rand()/100)
        noise.add_edge(76,53,weight=64*np.random.rand()/100)
        noise.add_edge(76,77,weight=64*np.random.rand()/100)
        noise.add_edge(77,52,weight=64*np.random.rand()/100)
        noise.add_edge(78,77,weight=64*np.random.rand()/100)
        noise.add_edge(51,78,weight=64*np.random.rand()/100)
        noise.add_edge(79,78,weight=64*np.random.rand()/100)
        noise.add_edge(79,50,weight=64*np.random.rand()/100)
        noise.add_edge(79,80,weight=64*np.random.rand()/100)
        noise.add_edge(49,80,weight=64*np.random.rand()/100)

    elif qpu_size == 10:

        noise.add_node(0,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(1,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(2,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(3,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(4,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(5,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(6,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(7,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(8,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(9,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(10,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(11,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(12,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(13,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(14,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(15,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(16,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(17,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(18,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(19,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(20,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(21,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(22,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(23,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(24,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(25,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(26,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(27,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(28,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(29,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(30,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(31,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(32,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(33,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(34,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(35,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(36,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(37,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(38,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(39,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(40,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(41,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(42,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(43,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(44,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(45,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(46,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(47,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(48,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(49,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(50,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(51,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(52,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(53,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(54,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(55,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(56,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(57,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(58,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(59,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(60,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(61,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(62,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(63,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(64,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(65,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(66,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(67,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(68,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(69,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(70,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(71,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(72,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(73,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(74,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(75,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(76,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(77,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(78,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(79,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(80,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(81,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(82,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(83,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(84,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(85,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(86,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(87,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(88,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(89,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(90,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(91,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(92,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(93,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(94,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(95,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(96,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(97,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(98,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_node(99,weight=128*np.random.rand()/1000,read_out=128*np.random.rand()/100)
        noise.add_edge(0,1,weight=128*np.random.rand()/100)
        noise.add_edge(0,13,weight=128*np.random.rand()/100)
        noise.add_edge(2,1,weight=128*np.random.rand()/100)
        noise.add_edge(12,1,weight=128*np.random.rand()/100)
        noise.add_edge(2,3,weight=128*np.random.rand()/100)
        noise.add_edge(2,11,weight=128*np.random.rand()/100)
        noise.add_edge(3,10,weight=128*np.random.rand()/100)
        noise.add_edge(3,4,weight=128*np.random.rand()/100)
        noise.add_edge(4,9,weight=128*np.random.rand()/100)
        noise.add_edge(5,4,weight=128*np.random.rand()/100)
        noise.add_edge(5,8,weight=128*np.random.rand()/100)
        noise.add_edge(6,5,weight=128*np.random.rand()/100)
        noise.add_edge(6,7,weight=128*np.random.rand()/100)
        noise.add_edge(7,20,weight=128*np.random.rand()/100)
        noise.add_edge(7,8,weight=128*np.random.rand()/100)
        noise.add_edge(8,19,weight=128*np.random.rand()/100)
        noise.add_edge(8,9,weight=128*np.random.rand()/100)
        noise.add_edge(9,18,weight=128*np.random.rand()/100)
        noise.add_edge(9,10,weight=128*np.random.rand()/100)
        noise.add_edge(10,11,weight=128*np.random.rand()/100)
        noise.add_edge(10,17,weight=128*np.random.rand()/100)
        noise.add_edge(16,11,weight=128*np.random.rand()/100)
        noise.add_edge(12,11,weight=128*np.random.rand()/100)
        noise.add_edge(12,15,weight=128*np.random.rand()/100)
        noise.add_edge(13,12,weight=128*np.random.rand()/100)
        noise.add_edge(13,14,weight=128*np.random.rand()/100)
        noise.add_edge(14,27,weight=128*np.random.rand()/100)
        noise.add_edge(14,15,weight=128*np.random.rand()/100)
        noise.add_edge(15,26,weight=128*np.random.rand()/100)
        noise.add_edge(16,15,weight=128*np.random.rand()/100)
        noise.add_edge(16,25,weight=128*np.random.rand()/100)
        noise.add_edge(17,16,weight=128*np.random.rand()/100)
        noise.add_edge(24,17,weight=128*np.random.rand()/100)
        noise.add_edge(17,18,weight=128*np.random.rand()/100)
        noise.add_edge(23,18,weight=128*np.random.rand()/100)
        noise.add_edge(18,19,weight=128*np.random.rand()/100)
        noise.add_edge(22,19,weight=128*np.random.rand()/100)
        noise.add_edge(19,20,weight=128*np.random.rand()/100)
        noise.add_edge(20,21,weight=128*np.random.rand()/100)
        noise.add_edge(21,34,weight=128*np.random.rand()/100)
        noise.add_edge(22,21,weight=128*np.random.rand()/100)
        noise.add_edge(22,33,weight=128*np.random.rand()/100)
        noise.add_edge(23,22,weight=128*np.random.rand()/100)
        noise.add_edge(23,32,weight=128*np.random.rand()/100)
        noise.add_edge(23,24,weight=128*np.random.rand()/100)
        noise.add_edge(31,24,weight=128*np.random.rand()/100)
        noise.add_edge(25,24,weight=128*np.random.rand()/100)
        noise.add_edge(25,30,weight=128*np.random.rand()/100)
        noise.add_edge(26,29,weight=128*np.random.rand()/100)
        noise.add_edge(26,27,weight=128*np.random.rand()/100)
        noise.add_edge(27,28,weight=128*np.random.rand()/100)
        noise.add_edge(28,41,weight=128*np.random.rand()/100)
        noise.add_edge(28,29,weight=128*np.random.rand()/100)
        noise.add_edge(29,40,weight=128*np.random.rand()/100)
        noise.add_edge(29,30,weight=128*np.random.rand()/100)
        noise.add_edge(30,39,weight=128*np.random.rand()/100)
        noise.add_edge(30,31,weight=128*np.random.rand()/100)
        noise.add_edge(38,31,weight=128*np.random.rand()/100)
        noise.add_edge(31,32,weight=128*np.random.rand()/100)
        noise.add_edge(32,37,weight=128*np.random.rand()/100)
        noise.add_edge(32,33,weight=128*np.random.rand()/100)
        noise.add_edge(36,33,weight=128*np.random.rand()/100)
        noise.add_edge(34,33,weight=128*np.random.rand()/100)
        noise.add_edge(34,35,weight=128*np.random.rand()/100)
        noise.add_edge(35,48,weight=128*np.random.rand()/100)
        noise.add_edge(35,36,weight=128*np.random.rand()/100)
        noise.add_edge(36,47,weight=128*np.random.rand()/100)
        noise.add_edge(36,37,weight=128*np.random.rand()/100)
        noise.add_edge(37,46,weight=128*np.random.rand()/100)
        noise.add_edge(38,37,weight=128*np.random.rand()/100)
        noise.add_edge(38,45,weight=128*np.random.rand()/100)
        noise.add_edge(38,39,weight=128*np.random.rand()/100)
        noise.add_edge(39,44,weight=128*np.random.rand()/100)
        noise.add_edge(39,40,weight=128*np.random.rand()/100)
        noise.add_edge(40,43,weight=128*np.random.rand()/100)
        noise.add_edge(40,41,weight=128*np.random.rand()/100)
        noise.add_edge(41,42,weight=128*np.random.rand()/100)
        noise.add_edge(42,43,weight=128*np.random.rand()/100)
        noise.add_edge(43,44,weight=128*np.random.rand()/100)
        noise.add_edge(44,45,weight=128*np.random.rand()/100)
        noise.add_edge(45,46,weight=128*np.random.rand()/100)
        noise.add_edge(46,47,weight=128*np.random.rand()/100)
        noise.add_edge(47,48,weight=128*np.random.rand()/100)
        noise.add_edge(49,48,weight=128*np.random.rand()/100)
        noise.add_edge(49,50,weight=128*np.random.rand()/100)
        noise.add_edge(47,50,weight=128*np.random.rand()/100)
        noise.add_edge(51,50,weight=128*np.random.rand()/100)
        noise.add_edge(46,51,weight=128*np.random.rand()/100)
        noise.add_edge(51,52,weight=128*np.random.rand()/100)
        noise.add_edge(52,45,weight=128*np.random.rand()/100)
        noise.add_edge(52,53,weight=128*np.random.rand()/100)
        noise.add_edge(44,53,weight=128*np.random.rand()/100)
        noise.add_edge(53,54,weight=128*np.random.rand()/100)
        noise.add_edge(43,54,weight=128*np.random.rand()/100)
        noise.add_edge(54,55,weight=128*np.random.rand()/100)
        noise.add_edge(42,55,weight=128*np.random.rand()/100)
        noise.add_edge(55,56,weight=128*np.random.rand()/100)
        noise.add_edge(57,56,weight=128*np.random.rand()/100)
        noise.add_edge(42,57,weight=128*np.random.rand()/100)
        noise.add_edge(41,58,weight=128*np.random.rand()/100)
        noise.add_edge(57,58,weight=128*np.random.rand()/100)
        noise.add_edge(58,59,weight=128*np.random.rand()/100)
        noise.add_edge(28,59,weight=128*np.random.rand()/100)
        noise.add_edge(60,59,weight=128*np.random.rand()/100)
        noise.add_edge(60,27,weight=128*np.random.rand()/100)
        noise.add_edge(61,60,weight=128*np.random.rand()/100)
        noise.add_edge(61,14,weight=128*np.random.rand()/100)
        noise.add_edge(62,61,weight=128*np.random.rand()/100)
        noise.add_edge(62,13,weight=128*np.random.rand()/100)
        noise.add_edge(62,63,weight=128*np.random.rand()/100)
        noise.add_edge(0,63,weight=128*np.random.rand()/100)
        noise.add_edge(64,63,weight=128*np.random.rand()/100)
        noise.add_edge(65,64,weight=128*np.random.rand()/100)
        noise.add_edge(62,65,weight=128*np.random.rand()/100)
        noise.add_edge(65,66,weight=128*np.random.rand()/100)
        noise.add_edge(61,66,weight=128*np.random.rand()/100)
        noise.add_edge(66,67,weight=128*np.random.rand()/100)
        noise.add_edge(60,67,weight=128*np.random.rand()/100)
        noise.add_edge(0,63,weight=128*np.random.rand()/100)
        noise.add_edge(67,68,weight=128*np.random.rand()/100)
        noise.add_edge(59,68,weight=128*np.random.rand()/100)
        noise.add_edge(68,69,weight=128*np.random.rand()/100)
        noise.add_edge(58,69,weight=128*np.random.rand()/100)
        noise.add_edge(69,70,weight=128*np.random.rand()/100)
        noise.add_edge(57,70,weight=128*np.random.rand()/100)
        noise.add_edge(71,70,weight=128*np.random.rand()/100)
        noise.add_edge(71,72,weight=128*np.random.rand()/100)
        noise.add_edge(71,56,weight=128*np.random.rand()/100)
        noise.add_edge(72,73,weight=128*np.random.rand()/100)
        noise.add_edge(56,73,weight=128*np.random.rand()/100)
        noise.add_edge(73,74,weight=128*np.random.rand()/100)
        noise.add_edge(55,74,weight=128*np.random.rand()/100)
        noise.add_edge(75,74,weight=128*np.random.rand()/100)
        noise.add_edge(75,54,weight=128*np.random.rand()/100)
        noise.add_edge(75,76,weight=128*np.random.rand()/100)
        noise.add_edge(76,53,weight=128*np.random.rand()/100)
        noise.add_edge(76,77,weight=128*np.random.rand()/100)
        noise.add_edge(77,52,weight=128*np.random.rand()/100)
        noise.add_edge(78,77,weight=128*np.random.rand()/100)
        noise.add_edge(51,78,weight=128*np.random.rand()/100)
        noise.add_edge(79,78,weight=128*np.random.rand()/100)
        noise.add_edge(79,50,weight=128*np.random.rand()/100)
        noise.add_edge(79,80,weight=128*np.random.rand()/100)
        noise.add_edge(49,80,weight=128*np.random.rand()/100)
        noise.add_edge(81,80,weight=128*np.random.rand()/100)
        noise.add_edge(81,82,weight=128*np.random.rand()/100)
        noise.add_edge(79,82,weight=128*np.random.rand()/100)
        noise.add_edge(83,82,weight=128*np.random.rand()/100)
        noise.add_edge(78,83,weight=128*np.random.rand()/100)
        noise.add_edge(84,83,weight=128*np.random.rand()/100)
        noise.add_edge(77,84,weight=128*np.random.rand()/100)
        noise.add_edge(85,84,weight=128*np.random.rand()/100)
        noise.add_edge(76,85,weight=128*np.random.rand()/100)
        noise.add_edge(85,86,weight=128*np.random.rand()/100)
        noise.add_edge(75,86,weight=128*np.random.rand()/100)
        noise.add_edge(86,87,weight=128*np.random.rand()/100)
        noise.add_edge(74,87,weight=128*np.random.rand()/100)
        noise.add_edge(88,87,weight=128*np.random.rand()/100)
        noise.add_edge(73,88,weight=128*np.random.rand()/100)
        noise.add_edge(88,89,weight=128*np.random.rand()/100)
        noise.add_edge(89,72,weight=128*np.random.rand()/100)
        noise.add_edge(90,89,weight=128*np.random.rand()/100)
        noise.add_edge(91,90,weight=128*np.random.rand()/100)
        noise.add_edge(72,91,weight=128*np.random.rand()/100)
        noise.add_edge(92,91,weight=128*np.random.rand()/100)
        noise.add_edge(92,71,weight=128*np.random.rand()/100)
        noise.add_edge(93,92,weight=128*np.random.rand()/100)
        noise.add_edge(93,70,weight=128*np.random.rand()/100)
        noise.add_edge(94,93,weight=128*np.random.rand()/100)
        noise.add_edge(69,94,weight=128*np.random.rand()/100)
        noise.add_edge(94,95,weight=128*np.random.rand()/100)
        noise.add_edge(95,68,weight=128*np.random.rand()/100)
        noise.add_edge(96,95,weight=128*np.random.rand()/100)
        noise.add_edge(67,96,weight=128*np.random.rand()/100)
        noise.add_edge(97,96,weight=128*np.random.rand()/100)
        noise.add_edge(66,97,weight=128*np.random.rand()/100)
        noise.add_edge(97,98,weight=128*np.random.rand()/100)
        noise.add_edge(99,98,weight=128*np.random.rand()/100)
        noise.add_edge(98,65,weight=128*np.random.rand()/100)
        noise.add_edge(64,99,weight=128*np.random.rand()/100)
        

    return noise 

###################################################################################################
#create traffic graph of our algorithm to be mapped
def traffic_graph(graph_counter):

    #martonosi
    # filename = ["hs2.qasm","hs4.qasm","hs6.qasm","bv4.qasm","bv6.qasm","bv8.qasm","toffoli.qasm","or.qasm","fredkin.qasm","peres.qasm","qft.qasm","adder.qasm"]
    #3x3 - 7
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm"]
    #4x4 -10
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm"]
    #5x5 - 12
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm","linear20.qasm","linear25.qasm"]
    #6x6 - 15
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm","linear20.qasm","linear25.qasm","linear30.qasm","linear35.qasm","linear36.qasm"]
    #7x7 - 18
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm","linear20.qasm","linear25.qasm","linear30.qasm","linear35.qasm","linear36.qasm","linear40.qasm","linear45.qasm","linear49.qasm"]
    #8x8 - 22
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm","linear20.qasm","linear25.qasm","linear30.qasm","linear35.qasm","linear36.qasm","linear40.qasm","linear45.qasm","linear49.qasm","linear50.qasm","linear55.qasm","linear60.qasm","linear64.qasm"]
    #9x9 - 27
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm","linear20.qasm","linear25.qasm","linear30.qasm","linear35.qasm","linear36.qasm","linear40.qasm","linear45.qasm","linear49.qasm","linear50.qasm","linear55.qasm","linear60.qasm","linear64.qasm","linear65.qasm","linear70.qasm","linear75.qasm","linear80.qasm","linear81.qasm"]
    #10x10 - 31
    # filename = ["linear3.qasm","linear4.qasm","linear5.qasm","linear6.qasm","linear7.qasm","linear8.qasm","linear9.qasm","linear10.qasm","linear15.qasm","linear16.qasm","linear20.qasm","linear25.qasm","linear30.qasm","linear35.qasm","linear36.qasm","linear40.qasm","linear45.qasm","linear49.qasm","linear50.qasm","linear55.qasm","linear60.qasm","linear64.qasm","linear65.qasm","linear70.qasm","linear75.qasm","linear80.qasm","linear81.qasm","linear85.qasm","linear90.qasm","linear95.qasm","linear100.qasm"]
    #sequence 1 - bfs,heuristic, and trivial - 36
    # filename = ["4QA.qasm","4QB.qasm","4QC.qasm","4QD.qasm","6QA.qasm","6QB.qasm","6QC.qasm","6QD.qasm","6QE.qasm","6QF.qasm","6QG.qasm","6QH.qasm","6QI.qasm","6QJ.qasm","6QK.qasm","8QA.qasm","8QB.qasm","8QC.qasm","8QD.qasm","8QE.qasm","8QF.qasm","8QG.qasm","8QH.qasm","8QI.qasm","8QJ.qasm","8QK.qasm","8QL.qasm","8QM.qasm","8QN.qasm","8QO.qasm","8QP.qasm","8QR.qasm","8QS.qasm","8QT.qasm","8QU.qasm","8QV.qasm"]
    #sequence 1 - bfs,heuristic, and trivial - depth 2x - 36
    filename = ["4QAD.qasm","4QBD.qasm","4QCD.qasm","4QDD.qasm","6QAD.qasm","6QBD.qasm","6QCD.qasm","6QDD.qasm","6QED.qasm","6QFD.qasm","6QGD.qasm","6QHD.qasm","6QID.qasm","6QJD.qasm","6QKD.qasm","8QAD.qasm","8QBD.qasm","8QCD.qasm","8QDD.qasm","8QED.qasm","8QFD.qasm","8QGD.qasm","8QHD.qasm","8QID.qasm","8QJD.qasm","8QKD.qasm","8QLD.qasm","8QMD.qasm","8QND.qasm","8QOD.qasm","8QPD.qasm","8QRD.qasm","8QSD.qasm","8QTD.qasm","8QUD.qasm","8QVD.qasm"]
    #sequence 2 - bfs,heuristic, and trivial - 30
    # filename = ["6QA.qasm","6QB.qasm","6QC2.qasm","6QD2.qasm","6QE2.qasm","6QF2.qasm","6QG2.qasm","6QH2.qasm","6QI2.qasm","6QJ2.qasm","6QK2.qasm","8QC2.qasm","8QD2.qasm","8QE2.qasm","8QF2.qasm","8QG2.qasm","8QH2.qasm","8QI2.qasm","8QJ2.qasm","8QK2.qasm","8QL2.qasm","8QM2.qasm","8QN2.qasm","8QO2.qasm","8QP2.qasm","8QR2.qasm","8QS2.qasm","8QT2.qasm","8QU2.qasm","8QV2.qasm"]
    #sequence 2 - bfs,heuristic, and trivial - depth 2x - 28
    # filename = ["6QC2D.qasm","6QD2D.qasm","6QE2D.qasm","6QF2D.qasm","6QG2D.qasm","6QH2D.qasm","6QI2D.qasm","6QJ2D.qasm","6QK2D.qasm","8QC2D.qasm","8QD2D.qasm","8QE2D.qasm","8QF2D.qasm","8QG2D.qasm","8QH2D.qasm","8QI2D.qasm","8QJ2D.qasm","8QK2D.qasm","8QL2D.qasm","8QM2D.qasm","8QN2D.qasm","8QO2D.qasm","8QP2D.qasm","8QR2D.qasm","8QS2D.qasm","8QT2D.qasm","8QU2D.qasm","8QV2D.qasm"]
    traffic = parser(filename[graph_counter])

    return traffic 
 
###################################################################################################
#heuristic algorithm
class heuristic:
 
    def __init__(self,noise,traffic):
        self.noise = noise
        self.traffic = traffic
        self.create_node_and_edge_dicts()
        self.allocate()
 
    def create_node_and_edge_dicts(self):
        self.edges = dict(self.noise.edges())
        set_1 = list(self.edges.keys())
        set_2 = list(self.edges.values())
        set_3 = {}
        inv_set_3 = {}
 
        for i in range(0,len(set_2)):      
            set_3.update({set_1[i]:set_2[i]['weight']})
 
        for j in range(0,len(set_2)):      
            inv_set_3.update({set_2[j]['weight']:set_1[j]})
 
        self.edges = set_3
        self.inv_edges = inv_set_3
        self.nodes = dict(self.noise.nodes(data='weight',default=1))
 
        self.inv_nodes = {}
        set_1 = list(self.nodes.keys())
        set_2 = list(self.nodes.values())
        for n in range(0,len(set_1)):
            self.inv_nodes.update({set_2[n]:set_1[n]})
 
    #calculate the traffic coefficient and allocate the first 2 qubits     
    def allocate(self):
        #designate an array of frequencies
        frequencies = []
        #start by calculating frequency for all nodes in traffic graph
        for a in range(0,len(self.traffic)):
            frequencies.append(self.traffic.nodes[a]['single'])
            for b in range(0,len(self.traffic)):
                if b in self.traffic[a]:
                    frequencies[a] += 2*self.traffic.edges[a,b]['double']
 
        #calculate traffic coefficients
        traf_coefs = [1/r for r in frequencies]
        traf_coefs = [1-s for s in traf_coefs]
 
        #define and calculate the normalization constant
        normalization = 0
        for c in range(0,len(traf_coefs)):
            normalization += traf_coefs[c]
        normalization = 1/normalization
 
        #outputs the normalized traffic coefficents
        normalized_traf_coefs = [normalization*u for u in traf_coefs]

        #calculation of traffic coefficents
        self.traf_qubits_and_coefs = {}
        self.traf_qubits_and_coefs_inverse = {}
        for i in range(0,len(traf_coefs)):
            self.traf_qubits_and_coefs.update({i:normalized_traf_coefs[i]})
        for key, value in self.traf_qubits_and_coefs.items():
            if value not in self.traf_qubits_and_coefs_inverse:
                self.traf_qubits_and_coefs_inverse[value] = [key]
            else:
                self.traf_qubits_and_coefs_inverse[value].append(key)

        #start the allocation process
        self.final_mapping = {}
        #just map a simple linear algorithm by selecting the best edges 
        for i in range(0,len(self.traf_qubits_and_coefs)):
            if len(self.final_mapping) == 0: 
                #need to ascertain the best connected nodes...
                degrees_noise = dict(self.noise.degree())
                degrees_noise = dict(sorted(degrees_noise.items(),key=operator.itemgetter(1),reverse=True))
                connectivity = max(degrees_noise.values())
                best_nodes = [keys for keys,values in degrees_noise.items() if int(values) >= max(degrees_noise.values())]
                #...and find the best edge error rate for one of these nodes, supremum error rate ... finds all edges linked to each best_connected node 
                error_edges = list(self.noise.edges(best_nodes))
                error_rates = []
                #makes a list of all error rates 
                for j in range(0,len(error_edges)):
                    error_rates.append(self.noise[error_edges[j][0]][error_edges[j][1]]['weight'])
                min_edge_rate = min(error_rates)
                mapp_noise_qubit = self.inv_edges[min_edge_rate]
                if mapp_noise_qubit[0] in best_nodes:
                    self.final_mapping.update({list(self.traf_qubits_and_coefs.keys())[i]:mapp_noise_qubit[0]})
                elif mapp_noise_qubit[0] not in best_nodes:
                    self.final_mapping.update({list(self.traf_qubits_and_coefs.keys())[i]:mapp_noise_qubit[1]}) 
            else:
                #find a list of all nodes that are distance "distance" away from first traff. coefficient qubit
                path_physical = nx.single_source_dijkstra_path_length(self.noise,self.final_mapping[list(self.traf_qubits_and_coefs.keys())[i-1]],cutoff=1)
                path_physical = dict(sorted(path_physical.items(),key=operator.itemgetter(1),reverse=False))
                path_physical = list(path_physical.keys())
                #cycle through the physically available nodes, and check availibility
                for k in range(0,len(path_physical)):
                    if path_physical[k] in self.final_mapping.values() and list(self.traf_qubits_and_coefs.keys())[i] in self.final_mapping.keys():
                        continue
                    elif path_physical[k] not in self.final_mapping.values() and list(self.traf_qubits_and_coefs.keys())[i] not in self.final_mapping.keys():
                        self.final_mapping.update({list(self.traf_qubits_and_coefs.keys())[i]:path_physical[k]})

###################################################################################################
#brute force algorithm
class brute:
     
    def __init__(self,noise,traffic):
        self.noise = noise
        self.traffic = traffic

        self.create_node_and_edge_dicts()
        self.permute_and_generate()

    def create_node_and_edge_dicts(self):
        self.edges = dict(self.noise.edges())
        set_1 = list(self.edges.keys())
        set_2 = list(self.edges.values())
        set_3 = {}
        inv_set_3 = {}
 
        for i in range(0,len(set_2)):      
            set_3.update({set_1[i]:set_2[i]['weight']})
 
        for j in range(0,len(set_2)):      
            inv_set_3.update({set_2[j]['weight']:set_1[j]})
 
        self.edges = set_3
        self.inv_edges = inv_set_3
        self.nodes = dict(self.noise.nodes(data='weight',default=1))
 
        self.inv_nodes = {}
        set_1 = list(self.nodes.keys())
        set_2 = list(self.nodes.values())
        for n in range(0,len(set_1)):
            self.inv_nodes.update({set_2[n]:set_1[n]})
 
    def permute_and_generate(self):
        #creates list of tuples for all possible permutations of the physical QPU 
        permutations = list(iter.permutations(self.nodes.keys()))  
        self.final_mapping = {} 
        list_final_score = []  

        #loops of all of the possible permutations
        for i in range(len(permutations)):
            permutation_phys_qubits = permutations[i]
            #loops over all v. qubits in algorithm
            for j in range(len(self.traffic)):
                self.final_mapping.update({j:permutation_phys_qubits[j]})
            #evaluate the metric
            self.brute = metric(self.noise,self.traffic,self.final_mapping)
            list_final_score.append(self.brute.final_metric_product)
            #list_final_score.append(self.brute.final_metric_logarithm)
        self.max_final_score = max(list_final_score)
        index_max_score = list_final_score.index(self.max_final_score)
        max_permutation_phys_qubits = permutations[index_max_score]
        for k in range(len(self.traffic)):
            self.final_mapping.update({k:max_permutation_phys_qubits[k]})

###################################################################################################
#no-mapping solution
class nomapper:

    def __init__(self,noise,traffic):
        self.noise = noise
        self.traffic = traffic

        self.create_node_and_edge_dicts()
        self.assign()
     
    def create_node_and_edge_dicts(self):
        self.edges = dict(self.noise.edges())
        set_1 = list(self.edges.keys())
        set_2 = list(self.edges.values())
        set_3 = {}
        inv_set_3 = {}
 
        for i in range(0,len(set_2)):      
            set_3.update({set_1[i]:set_2[i]['weight']})
 
        for j in range(0,len(set_2)):      
            inv_set_3.update({set_2[j]['weight']:set_1[j]})
 
        self.edges = set_3
        self.inv_edges = inv_set_3
        self.nodes = dict(self.noise.nodes(data='weight',default=1))
 
        self.inv_nodes = {}
        set_1 = list(self.nodes.keys())
        set_2 = list(self.nodes.values())
        for n in range(0,len(set_1)):
            self.inv_nodes.update({set_2[n]:set_1[n]})
    
    def assign(self):
        #assign 1-to-1 to self.final_mapping
        self.final_mapping = {} 
        for i in range(0,len(self.nodes.keys())):
            self.final_mapping.update({i:i})

###################################################################################################
#calculate the basic product metric
class metric:
 
    def __init__(self,noise,traffic,final_mapping):
        self.noise = noise
        self.traffic = traffic
        self.final_mapping = final_mapping
        self.create_node_and_edge_dicts()

        self.calculate_metric()
 
    def calculate_metric(self):
        self.single_gate_product_metric()
        self.SWAP_double_gate_product_metric()
        # self.calculate_normalization()
 
    def create_node_and_edge_dicts(self):
        self.edges = dict(self.noise.edges())
        set_1 = list(self.edges.keys())
        set_2 = list(self.edges.values())
        set_3 = {}
        inv_set_3 = {}
 
        for i in range(0,len(set_2)):      
            set_3.update({set_1[i]:set_2[i]['weight']})
 
        for j in range(0,len(set_2)):      
            inv_set_3.update({set_2[j]['weight']:set_1[j]})
 
        self.edges = set_3
        self.inv_edges = inv_set_3
        self.nodes = dict(self.noise.nodes(data='weight',default=1))
 
        self.inv_nodes = {}
        set_1 = list(self.nodes.keys())
        set_2 = list(self.nodes.values())
        for n in range(0,len(set_1)):
            self.inv_nodes.update({set_2[n]:set_1[n]})
 
    def single_gate_product_metric(self):
        #dictionary of form {algorithm:single_gate_frequency...}
        single_invocation = nx.get_node_attributes(self.traffic,'single')
        # print("single_invocation = ",single_invocation)
        #single error rate for the product metric 
        self.single_product = 1
        #cycles through the dictionary single_invocation
        for key,val in single_invocation.items():
            #extracts the error rate for a node
            error_rate_single = self.nodes[self.final_mapping[key]]
            self.single_product = self.single_product*((1-error_rate_single)**single_invocation[key])
 
    def SWAP_double_gate_product_metric(self):
        #set initial overall double-gate and SWAP errors
        double_invocation = nx.get_edge_attributes(self.traffic,'double')
        #outputs list form of the algorithm edges in tuples
        algorithmic_edges = list(double_invocation.keys())
        #set summations for the gate invocations
        current_swap_invocation_number_sum = 0
        double_gate_invocations_sum = 0
        #set the error rate for each portion of the product metric
        self.double_product = 1 
        self.swap_product = 1
        self.final_metric_product = 1
        #cycle through list of tuples and find their positions on physical lattice
        for j in range(0, len(algorithmic_edges)):
            #find the distance between the two nodes á la Dijkstra
            distance = nx.shortest_path(self.noise,source=self.final_mapping[algorithmic_edges[j][0]],target=self.final_mapping[algorithmic_edges[j][1]])
            #if the size of distance is 1 - then it is a double-gate error problem
            if len(distance) == 2:
                #find the error rate for physical edge used
                error_rate_product = self.noise[distance[0]][distance[1]]['weight']
                #find number of double gate iterations
                double_gate_invocations = self.traffic[algorithmic_edges[j][0]][algorithmic_edges[j][1]]['double']
                #multiply by the swap and double-gate error rate
                self.double_product = self.double_product*((1-error_rate_product)**double_gate_invocations)
            #if the size of distance is not 1 - then it is a SWAP-gate error problem
            elif len(distance) > 2:
                list_error_rates_product = []
                #cycle through the list of physical qubits used and find error rates
                for i in range(0,len(distance)-1):
                    #find the error rate for physical edge used
                    list_error_rates_product.append([distance[i],distance[i+1]])
                    list_error_rates_product = list_error_rates_product[0]
                    #adds the physical qubits to new variable for only the corresponding error rates 
                    list_error_rates_metric = self.noise[list_error_rates_product[0]][list_error_rates_product[1]]
                    list_error_rates_product = []
                    #multiply the error rates together
                    list_error_rates_metric_base = 1
                    list_error_rates_metric_base = (1-list_error_rates_metric['weight'])*list_error_rates_metric_base
                    success_rates = 1 
                    success_rates = (1-list_error_rates_metric['weight'])*list_error_rates_metric_base
                #find the number of double-gate invocations needed for the SWAP route - multiply everything by this number
                current_swap_invocation_number = self.traffic[algorithmic_edges[j][0]][algorithmic_edges[j][1]]['double']
                #final calculation
                self.swap_product = self.swap_product*(success_rates**(current_swap_invocation_number*2))
             
        #final calculation for the overall error rate for single, double, and swap gates
        self.final_metric_product = self.swap_product*self.double_product*self.single_product
        # print("error_rate_before_adding_measurement_errors = ",self.final_metric_product)

        #incorporate measurement errors
        read_out_invocation = nx.get_node_attributes(self.noise,'read_out')
        self.read_out_error = 1
        #cycles through the dictionary read_out_invocation
        for key,val in self.final_mapping.items():
            #extracts the error rate for a node
            error_rate_read_out = read_out_invocation[self.final_mapping[key]]
            self.read_out_error = self.read_out_error*(1-error_rate_read_out)
        self.final_metric_product = self.final_metric_product*self.read_out_error

###################################################################################################
#calculation of statistics 
def data_analysis(set_metric_evals,set_metric_evals_brute,set_number_benchmarks):
    average_metric_eval = []
    average_metric_eval_brute = []
    average_metric_eval_nomapper = []

    set_number_benchmarks = set_number_benchmarks

    for graph_counter in range(0,set_number_benchmarks):
        average_metric_eval.append(sum(set_metric_evals[:,graph_counter])/len(set_metric_evals))
        average_metric_eval_brute.append(sum(set_metric_evals_brute[:,graph_counter])/len(set_metric_evals_brute))
        average_metric_eval_nomapper.append(sum(set_metric_evals_nomapper[:,graph_counter])/len(set_metric_evals_nomapper))

    print("Heuristic Results = ",average_metric_eval)
    print("Brute-Force Results = ",average_metric_eval_brute)
    print("Trivial-Mapping Results = ",average_metric_eval_nomapper)
    #3x3
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9"]
    #4x4
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16"]
    #5x5
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16","hL20","tL20","hL25","tL25"]
    #6x6
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16","hL20","tL20","hL25","tL25","hL30","tL30","hL35","tL35","hL36","tL36"]
    #7x7
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16","hL20","tL20","hL25","tL25","hL30","tL30","hL35","tL35","hL36","tL36","hL40","tL40","hL45","tL45","hL49","tL49"]
    #8x8
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16","hL20","tL20","hL25","tL25","hL30","tL30","hL35","tL35","hL36","tL36","hL40","tL40","hL45","tL45","hL49","tL49","hL50","tL50","hL55","tL55","hL60","tL60","hL64","tL64"]
    #9x9
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16","hL20","tL20","hL25","tL25","hL30","tL30","hL35","tL35","hL36","tL36","hL40","tL40","hL45","tL45","hL49","tL49","hL50","tL50","hL55","tL55","hL60","tL60","hL64","tL64","hL64","tL645","hL65","tL70","hL70","tL75","hL75","tL80","hL81","tL81"]
    #10x10
    # objects = ["hL3","tL3","hL4","tL4","hL5","tL5","hL6","tL6","hL7","tL7","hL8","tL8","hL9","tL9","hL10","tL10","hL15","tL15","hL16","tL16","hL20","tL20","hL25","tL25","hL30","tL30","hL35","tL35","hL36","tL36","hL40","tL40","hL45","tL45","hL49","tL49","hL50","tL50","hL55","tL55","hL60","tL60","hL64","tL64","hL64","tL645","hL65","tL70","hL70","tL75","hL75","tL80","hL81","tL81","hL85","tL85","hL90","tL90","hL95","tL95","hL100","tL100"]
    #sequence1
    # objects = ["b4QA","h4QA","t4QA","b4QB","h4QB","t4QB","b4QC","h4QC","t4QC","b4QD","h4QD","t4QD","b6QA","h6QA","t6QA","b6QB","h6QB","t6QB","b6QC","h6QC","t6QC","b6QD","h6QD","t6QD","b6QE","h6QE","t6QE","b6QF","h6QF","t6QF","b6QG","h6QG","t6QG","b6QH","h6QH","t6QH","b6QI","h6QI","t6QI","b6QJ","h6QJ","t6QJ","b6QK","h6QK","t6QK","b8QA","h8QA","t8QA","b8QB","h8QB","t8QB","b8QC","h8QC","t8QC","b8QD","h8QD","t8QD","b8QE","h8QE","t8QE","b8QF","h8QF","t8QF","b8QG","h8QG","t8QG","b8QH","h8QH","t8QH","b8QI","h8QI","t8QI","b8QJ","h8QJ","t8QJ","b8QK","h8QK","t8QK","b8QL","h8QL","t8QL","b8QM","h8QM","t8QM","b8QN","h8QN","t8QN","b8QO","h8QO","t8QO","b8QP","h8QP","t8QP","b8QR","h8QR","t8QR","b8QS","h8QS","t8QS","b8QT","h8QT","t8QT","b8QU","h8QU","t8QU","b8QV","h8QV","t8QV"]
    #sequence2 
    # objects = ["b6QC","h6QC","t6QC","b6QD","h6QD","t6QD","b6QE","h6QE","t6QE","b6QF","h6QF","t6QF","b6QG","h6QG","t6QG","b6QH","h6QH","t6QH","b6QI","h6QI","t6QI","b6QJ","h6QJ","t6QJ","b6QK","h6QK","t6QK","b8QC","h8QC","t8QC","b8QD","h8QD","t8QD","b8QE","h8QE","t8QE","b8QF","h8QF","t8QF","b8QG","h8QG","t8QG","b8QH","h8QH","t8QH","b8QI","h8QI","t8QI","b8QJ","h8QJ","t8QJ","b8QK","h8QK","t8QK","b8QL","h8QL","t8QL","b8QM","h8QM","t8QM","b8QN","h8QN","t8QN","b8QO","h8QO","t8QO","b8QP","h8QP","t8QP","b8QR","h8QR","t8QR","b8QS","h8QS","t8QS","b8QT","h8QT","t8QT","b8QU","h8QU","t8QU","b8QV","h8QV","t8QV"]
    # performance = []
    # colors = []
    # for alpha in range(0,set_number_benchmarks):
    #     # brute = average_metric_eval_brute[alpha].round(decimals=3)
    #     heuristic = average_metric_eval[alpha].round(decimals=3)
    #     nomapper = average_metric_eval_nomapper[alpha].round(decimals=3)
    #     # performance.append(brute)
    #     performance.append(heuristic)
    #     performance.append(nomapper)
    #     # colors.append('r')
    #     colors.append('b')
    #     colors.append('g')
    
    # #plotter portion
    # y_pos = np.arange(len(objects))

    # bars = plt.bar(y_pos, performance, width=0.90, align='center', alpha=0.5, color=colors)
    # plt.xticks(y_pos, objects, fontsize=7,rotation=90)
    # plt.ylabel('success rate')
    # plt.yticks(np.arange(0, 1, 0.05))
    # plt.tick_params(labeltop=False, labelright=True,labelbottom=True,labelleft=True)
    # plt.title('Success-Rate Results')
    # plt.ylim(0.0, 1.0)
    # for bar in bars:
    #     yval = bar.get_height()
    #     plt.text(bar.get_x(), yval + .005, yval)
    # plt.tight_layout()
    # plt.show()

###################################################################################################

trials = 100
set_number_benchmarks = 36
set_metric_evals = np.zeros((trials,set_number_benchmarks),float)
set_metric_evals_brute = np.zeros((trials,set_number_benchmarks),float)
set_metric_evals_nomapper = np.zeros((trials,set_number_benchmarks),float)
time_brute = []
time_heuristic = [] 
time_trivial = []

for graph_counter in range(0,set_number_benchmarks):
    for l in range(0,trials):
        x = noise_graph()
        y = traffic_graph(graph_counter)

        #heuristic code 
        start = time.time()
        hue = heuristic(x,y)
        metric_heuristic = metric(hue.noise,hue.traffic,hue.final_mapping)
        set_metric_evals[l,graph_counter] = metric_heuristic.final_metric_product
        end = time.time()
        time_heuristic.append((end-start))

        #brute-force code
        start = time.time()
        bruteforce = brute(x,y)
        metric_brute = metric(bruteforce.noise,bruteforce.traffic,bruteforce.final_mapping)
        set_metric_evals_brute[l,graph_counter] = metric_brute.final_metric_product
        end = time.time()
        time_brute.append((end-start))
        # set_metric_evals_brute = 0

        #no-mapping solution
        start = time.time()
        nomapp = nomapper(x,y)
        metric_nomapp = metric(nomapp.noise,nomapp.traffic,nomapp.final_mapping)
        set_metric_evals_nomapper[l,graph_counter] = metric_nomapp.final_metric_product
        end = time.time()
        time_trivial.append((end-start))
    print("graph completed = ",graph_counter)

time_brute = sum(time_brute)/(len(time_brute))
time_heuristic = sum(time_heuristic)/(len(time_heuristic))
time_trivial = sum(time_trivial)/(len(time_trivial))

print("BFS time: ",time_brute)
print("Heuristic time: ",time_heuristic)
print("Trivial time: ",time_trivial)

data_analysis(set_metric_evals,set_metric_evals_brute,set_number_benchmarks)

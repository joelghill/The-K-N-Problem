# Joel Hill
# jgh719
# 10344729

import networkx as nx
import matplotlib.pyplot as plt
# import statespace as state

#following example of networkx graph

#G=nx.Graph()
#G=nx.random_regular_graph(4,15)
#G = nx.navigable_small_world_graph(4,1,2,2,2)
#G = nx.random_geometric_graph(8, 1)
G = nx.Graph()
G.add_node("a")
G.add_nodes_from(["b", "c"])

G.add_edge(1, 2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

#print(G.nodes())
#print(G.edges())

#print(type(G.nodes()))
#print(type(G.edges()))

# adding just one node:
#G.add_node("a")
# a list of nodes:
#G.add_nodes_from(["b","c"])

#print("Nodes of graph: ")
#print(G.nodes())
#print("Edges of graph: ")
#print(G.edges())

#add edges to graph
#G.add_edge(1,2)
#edge = ("d", "e")
#G.add_edge(*edge)
#edge = ("a", "b")
#G.add_edge(*edge)

#print("Nodes of graph: ")
#print(G.nodes())
#print("Edges of graph: ")
#print(G.edges())

# adding a list of edges:
#G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

#print the resulting graph by using matplotlib:
nx.draw(G, with_labels=True)
plt.savefig("simple_path.png")  # save as png
plt.show()  # display

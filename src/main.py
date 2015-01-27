# Joel Hill
# jgh719
# 10344729

import networkx as nx
import matplotlib.pyplot as plt

#following example of networkx graph

G=nx.Graph()

print(G.nodes())
print(G.edges())

print(type(G.nodes()))
print(type(G.edges()))

# adding just one node:
G.add_node("a")
# a list of nodes:
G.add_nodes_from(["b","c"])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

#add edges to graph
G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

#print the resulting graph by using matplotlib:
nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display
#fig = G.get_figure()
#fig.savefig("output.png")
import json 
import csv
import operator
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from random import random

def draw_graph(nodes, edges, show_details):
    G = nx.Graph()
    mapping = {}
    counter = 1

    for n in nodes:
        mapping[n] = counter
        counter += 1 

    for e in edges:
        G.add_edge(mapping[e[0]], mapping[e[1]], weight=e[2])

    print mapping
    edge_labels = dict([((u,v,),d['weight'])
            for u,v,d in G.edges(data=True)])

    pos = nx.circular_layout(G)
    colors=range(len(edges))
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels) 
    nx.draw_circular(G, scale=2, node_size=4000, node_color="#DC97C8", edge_color=colors, width=4, edge_cmap=plt.cm.RdPu)
    plt.show()

def write_nodes(nodes, shows_list, show_details):
    print "Writing nodes"
    header = "Id,Label,Seasons\n"
    with open("gephi_data/top_tvn1_nodes.csv", "a") as outfile:
        outfile.write(header)

    for node in nodes:
        name = shows_list[node]["name"]
        year = shows_list[node]["year"]
        seasons = show_details[node]["seasons"]
        out = "%s,%s %s,%s\n" % (node, name, year, seasons)
        with open("gephi_data/top_tvn1_nodes.csv", "a") as outfile:
            outfile.write(out.encode("ascii", "ignore"))

def write_edges(edges, shows_list, show_details):
    print "Writing edges"
    header = "source,target,type,weight\n"
    with open("gephi_data/top_tvn1_edges.csv", "a") as outfile:
        outfile.write(header)

    counter = 0
    for e in edges[-10:]:
        out = "%s,%s,%s,%s\n" % (e[0], e[1], "Undirected", e[2])
        with open("gephi_data/top_tvn1_edges.csv", "a") as outfile:
            outfile.write(out.encode("ascii", "ignore"))

def main():
    print "Loading JSON files"
    shows_list = json.load(file("data/shows_list_with_years.json", "r"))
    show_details = json.load(file("data/show_details_1.json", "r"))
    show_details.update(json.load(file("data/show_details_2.json", "r")))

    print "Getting 10 shows that share the most actors"
    lines = csv.reader(open("gephi_data/tvn1_edges.csv"))
    lines.next()
    nodes = set()
    edges = []
    for l in lines:
        edges.append((l[0], l[1], int(l[3].strip())))

    edges.sort(key=operator.itemgetter(2))
    for e in edges[-10:]:
        nodes.add(e[0])
        nodes.add(e[1])

    #write_edges(edges[-10:], shows_list, show_details)
    #write_nodes(nodes, shows_list, show_details)
    draw_graph(nodes, edges[-10:], show_details)

if __name__ == "__main__":
    main()
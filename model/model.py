import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.allTeams = []
        self.grafo = nx.Graph()

    def buildGraph(self):
        self.grafo.clear()
        if len(self.allTeams) == 0:
            print("Lista squadre vuota")
            return
        self.grafo.add_nodes_from(self.allTeams)


        myedges = list(itertools.combinations(self.allTeams, 2))

        self.grafo.add_edges_from(myedges)

        #print(myedges)

        # for t1 in self.grafo.nodes:
        #     for t2 in self.grafo.nodes:
        #         if t1 != t2:
        #             self.grafo.add_edge(t1, t2)

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self.allTeams = DAO.getTeamsOfYear(year)
        return self.allTeams

    def printGraphDetails(self):
        print(f"Grafo creato con {len(self.grafo.nodes)} nodi e {len(self.grafo.edges)} archi")


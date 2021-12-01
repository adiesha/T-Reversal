import networkx as nx
from matplotlib import pylab as plt


class TranspositionGraph():
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.adj = self.findAdj(s)
        self.adjadjs = self.findadjofadj(self.s, self.adj)
        self.adjadjt = self.findadjofadj(self.t, self.adj)
        self.countofadj = len(self.adj)
        self.G = nx.MultiDiGraph()

    def findAdj(self, s):
        adj = {}
        count = 0

        for i in range(len(s) - 1):
            if s[i:(i + 2)] not in adj:
                adj[s[i:(i + 2)]] = count
                count += 1

        return adj

    def findadjofadj(self, s, adj):
        adjadj = []
        for i in range(len(s) - 1):
            adjadj.append(adj[s[i:i + 2]])
        return adjadj

    def getVin(self, i):
        return 2 * i

    def getVout(self, i):
        return (2 * i) + 1

    def createGraph(self, G, adjofadj):
        pos = {}
        for i in range(len(adjofadj) - 1):
            vout = str(adjofadj[i]) + "o"
            vin = str(adjofadj[i + 1]) + "i"
            G.add_edge(vout, vin)
            if vout not in pos:
                pos[vout] = (2*adjofadj[i], 2)
            if vin not in pos:
                pos[vin] = (2*adjofadj[i + 1] + 1, 2)
        return G, pos

    def drawGraph(self, G, pos=None):

        # pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, connectionstyle="arc3,rad=0.9", style='dotted', )

        # nx.draw_networkx_edges(G, pos=nx.spring_layout(G), connectionstyle=f'arc3,rad=3')
        # nx.draw_networkx_edge_labels(G, pos, font_size=7)
        plt.show()


def main():
    tg = TranspositionGraph("123432341214", "123434123214")
    print(tg.adjadjs)
    G, pos = tg.createGraph(tg.G, tg.adjadjs)
    tg.drawGraph(G, pos)
    print(G.size())
    print(G["2o"])
    print(G.edges("1o"))
    print(G.edges("0o"))
    G, pos = tg.createGraph(tg.G, tg.adjadjt)
    tg.drawGraph(G, pos)
    print(G.size())


if __name__ == '__main__':
    main()

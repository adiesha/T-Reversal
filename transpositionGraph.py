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
                pos[vout] = (2 * adjofadj[i] + 1, 2)
            if vin not in pos:
                pos[vin] = (2 * adjofadj[i + 1], 2)
        return G, pos

    def drawGraph(self, G, pos=None, connectionstyle="arc3,rad=0.4", edge_color='red'):

        # pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, connectionstyle=connectionstyle, style='dotted', edge_color=edge_color)

        # nx.draw_networkx_edges(G, pos=nx.spring_layout(G), connectionstyle=f'arc3,rad=3')
        # nx.draw_networkx_edge_labels(G, pos, font_size=7)
        plt.show()

    def drawTwoGraphsOnSameThing(self, G1, G2, pos1, pos2, connectionstyle1="arc3,rad=0.4",
                                 connectionstyle2="arc3,rad=0.7", edge_color1='red', edge_color2='green'):
        G3 = nx.compose(G1, G2)
        pos3 = pos1.update(pos2)
        nx.draw(G3, pos1, with_labels=True, nodelist=G1.nodes(), edgelist=G1.edges(), edge_color=edge_color1,
                connectionstyle=connectionstyle1)
        nx.draw(G3, pos1, with_labels=True, nodelist=G2.nodes(), edgelist=G2.edges(), edge_color=edge_color2,
                connectionstyle=connectionstyle2)
        plt.show()


def test(s1, s2):
    tg = TranspositionGraph(s1, s2)
    G1 = nx.MultiDiGraph()
    G1, pos1 = tg.createGraph(G1, tg.adjadjs)

    G2 = nx.MultiDiGraph()
    G2, pos2 = tg.createGraph(G2, tg.adjadjt)

    tg.drawTwoGraphsOnSameThing(G1, G2, pos1, pos2)


def main():
    test("123432341214", "123434123214")
    test("123213234144", "144132123234")


if __name__ == '__main__':
    main()

#
#     tg = TranspositionGraph("123432341214", "123434123214")
#     print(tg.adjadjs)
#     G1 = nx.MultiDiGraph()
#     G1, pos1 = tg.createGraph(G1, tg.adjadjs)
#     tg.drawGraph(G1, pos1, "arc3,rad=0.6", edge_color='blue')
#     print(G1.size())
#     print(G1["2o"])
#     print(G1.edges("1o"))
#     print(G1.edges("0o"))
#
#     G2 = nx.MultiDiGraph()
#     G2, pos2 = tg.createGraph(G2, tg.adjadjt)
#     tg.drawGraph(G2, pos2, edge_color='green')
#     print(G2.size())
#
#     tg.drawTwoGraphsOnSameThing(G1, G2, pos1, pos2)

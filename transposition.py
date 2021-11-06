import networkx as nx
from matplotlib import pyplot as plt


class Transposition():
    def __init__(self):
        pass

    def dotransposition(self, s, character):
        indices = self.getcharacterIndices(s, character)
        i1 = indices[0]
        i2 = indices[1]
        i3 = indices[2]
        s1 = s[:i1]
        s2 = s[i1:i2]
        s3 = s[i2:i3]
        s4 = s[i3:]
        v = s1 + s3 + s2 + s4
        return v

    def getcharacterIndices(self, s, c):
        index = 0
        values = []
        for i in s:
            if i == c:
                values.append(index)
            index += 1
        return values


def main1():
    tr = Transposition()
    configs = {}
    # s = "331121223"
    # s = "513125154243423"
    s = "122334451554231"
    count = 0
    if s not in configs:
        configs[s] = count
        count += 1
    while True:
        c = input("")
        if c == "x":
            break
        s = tr.dotransposition(s, c)
        if s not in configs:
            configs[s] = count
            count += 1
        print(s)
    print(configs)


def dooperations(s, tr, configs, count, G, alphabet, nooflevels, prev, prevoperation="$"):
    for l in alphabet:
        if l == prevoperation:
            continue
        s = tr.dotransposition(s, l)
        if s not in configs:
            configs[s] = count
            count += 1
        if G.has_node(prev) and G.degree[prev] == 3:
            print(prev)
        if not G.has_edge(prev, configs[s]):
            G.add_edge(prev, configs[s], w=l)
        if nooflevels == 1:
            s = tr.dotransposition(s, l)
        else:
            count = dooperations(s, tr, configs, count, G, alphabet, nooflevels - 1, configs[s], l)
            s = tr.dotransposition(s, l)

    return count


def main2():
    tr = Transposition()
    s = "122334451554231"
    configs = {}
    count = 0
    configs[s] = count
    prev = count
    count += 1
    G = nx.Graph()
    alphabet = sorted(list(set(s)))
    count = dooperations(s, tr, configs, count, G, alphabet, 5, prev, "$")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, font_size=7)
    plt.show()
    print(configs)


if __name__ == '__main__':
    main1()
    main2()

    # tr = Transposition()
    # configs = {}
    # # s = "331121223"
    # # s = "513125154243423"
    # s = "123214341234"
    # # alphabet = list(set(s))
    # # count = 1
    # # configs[s] = 1
    # # count += 1
    # # for a in alphabet:
    # #     s = tr.dotransposition(s, a)
    # #     if s in configs:
    # #         pass
    # #     else:
    # #         print("New config found")
    # #         configs[s] = count
    # #         count += 1
    # # print(configs)
    # count = 0
    # if s not in configs:
    #     configs[s] = count
    #     count += 1
    # while True:
    #     c = input("")
    #     if c == "x":
    #         break
    #     s = tr.dotransposition(s, c)
    #     if s not in configs:
    #         configs[s] = count
    #         count += 1
    #     print(s)
    # print(configs)
    #
    # s = "123212341434"
    # configs2 = {}
    # count = 0
    # configs2[s] = count
    # prev = count
    # count += 1
    # G = nx.Graph()
    # alphabet = list(set(s))
    # for a in alphabet:
    #     s = tr.dotransposition(s, a)
    #     if s not in configs2:
    #         configs2[s] = count
    #         count += 1
    #     G.add_edge(prev, configs2[s], weight=a)
    #     prev1 = configs2[s]
    #     for b in alphabet:
    #         if b == a:
    #             continue
    #         s = tr.dotransposition(s, b)
    #         if s not in configs2:
    #             configs2[s] = count
    #             count += 1
    #         G.add_edge(prev1, configs2[s], weight=b)
    #         prev2 = configs2[s]
    #         for c in alphabet:
    #             if c == b:
    #                 continue
    #             s = tr.dotransposition(s, c)
    #             if s not in configs2:
    #                 configs2[s] = count
    #                 count += 1
    #             G.add_edge(prev2, configs2[s], weight=c)
    #             prev3 = configs2[s]
    #             for d in alphabet:
    #                 if d == c:
    #                     continue
    #                 s = tr.dotransposition(s, d)
    #                 if s not in configs2:
    #                     configs2[s] = count
    #                     count += 1
    #                 G.add_edge(prev3, configs2[s], weight=d)
    #                 s = tr.dotransposition(s, d)
    #             s = tr.dotransposition(s, c)
    #         s = tr.dotransposition(s, b)
    #     s = tr.dotransposition(s, a)
    #
    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, font_weight='bold')
    # nx.draw_networkx_edge_labels(G, pos, font_size=7)
    # plt.show()
    # print(configs2)

# Negative example for transposition?
# 12231332 -?> 122132331, 122312331
#
#
#
#
#
#
#
#

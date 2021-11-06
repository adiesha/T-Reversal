import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt


def main():
    G = nx.Graph()
    G.add_edge(1, 2)
    print(G.has_edge(2,1))
    nx.draw(G)
    plt.show()
    perms = list(itertools.permutations("012345"))

    nOfperms = len(perms)

    rand1 = random.randint(0, nOfperms - 1)
    rand2 = random.randint(0, nOfperms - 1)

    s = ''.join(perms[rand1]) + ''.join(perms[rand2])
    print(s)
    analyze(s)
    s = rev(s, "2")
    analyze(s)
    s = rev(s, "3")
    analyze(s)
    s = rev(s, "1")
    analyze(s)
    s = rev(s, "0")
    analyze(s)
    s = rev(s, "4")
    analyze(s)
    s = rev(s, "2")
    analyze(s)
    s = rev(s, "3")
    analyze(s)
    s = rev(s, "1")
    analyze(s)
    s = rev(s, "0")
    analyze(s)
    s = rev(s, "4")
    analyze(s)


def rev(s, c):
    print("reversing " + c)
    revs = s[::-1]
    first = s.index(c)
    last = len(s) - 1 - revs.index(c)

    # print(s[0:first + 1])
    # print(s[first + 1:last])
    # print(s[first + 1:last][::-1])
    # print(s[last:])

    result = s[0:first + 1] + s[first + 1:last][::-1] + s[last:]
    print(result)
    return result

    # result = s[0:first-1] + s[first:last][::-1] + s[last:-1]
    # print(result)


def analyze(s):
    alphabet = list(set(s))
    # print(alphabet)
    anadict = dict.fromkeys(alphabet)
    adjdict = dict.fromkeys(alphabet)
    # print(anadict)
    revs = s[::-1]
    i = 0
    for c in s:
        first = s.index(c)
        last = len(s) - 1 - revs.index(c)
        anadict[c] = list(s[first + 1:last])
        i += 1

    i = 0
    for c in s:
        # print adjacency list
        first = s.index(c)
        last = len(s) - 1 - revs.index(c)
        l = []
        if first - 1 >= 0:
            l.append(s[first - 1])
        if first + 1 < len(s):
            l.append(s[first + 1])
        if last - 1 >= 0:
            l.append(s[last - 1])
        if last + 1 < len(s):
            l.append(s[last + 1])
        adjdict[c] = l
        i = +1

    # print("middle characters: " + str(anadict))
    # print("adj characters" + str(adjdict))


if __name__ == '__main__':
    main()

# Python program to print all permutations

# from itertools import permutations
#
# print[''.join(p)
# for p in permutations('ABC')]
# # This code is contributed by Vidit Varshney
# Output:
# ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

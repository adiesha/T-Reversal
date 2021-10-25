class treversal():
    def __init__(self):
        pass

    def rev(self, s, c):
        # print("Reversing " + c)
        revs = s[::-1]
        first = s.index(c)
        last = len(s) - 1 - revs.index(c)

        result = s[0:first + 1] + s[first + 1:last][::-1] + s[last:]
        print(result)
        return result


    def analyze(self, s):
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

        print("middle characters: " + str(anadict))
        print("adj characters" + str(adjdict))

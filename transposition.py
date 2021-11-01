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


if __name__ == '__main__':
    tr = Transposition()
    configs = {}
    s = "1234143213241"
    # alphabet = list(set(s))
    # count = 1
    # configs[s] = 1
    # count += 1
    # for a in alphabet:
    #     s = tr.dotransposition(s, a)
    #     if s in configs:
    #         pass
    #     else:
    #         print("New config found")
    #         configs[s] = count
    #         count += 1
    # print(configs)
    while True:
        c = input("")
        if c == "x":
            break
        s = tr.dotransposition(s, c)
        print(s)
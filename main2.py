from treversal import treversal


def main():
    s = input("Input the string\n")

    t = treversal()
    while True:
        a = input("Enter option\n")
        if a == "a":
            t.analyze(s)
        elif a.isnumeric():
            s = t.rev(s, a)
        else:
            break


if __name__ == '__main__':
    main()

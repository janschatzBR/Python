def tabuada():
    tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1

tabuada()

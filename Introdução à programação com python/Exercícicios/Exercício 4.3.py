n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if n1 > n2 and n1 > n3:#n1 maior de todos
    print("Maior é n1")
    if n2 < n3:
        print("Menor é n2")
    else:
        print("Menor é n3")
else:
    if n2 > n1 and n2 > n3: #n2 é maior de todos
        print("Maior é n2")
        if n1 < n3:
            print("Menor é n1")
        else:
            print("Menor é n3")

    else:
        print("Maior é n3")
        if n1 < n2:
            print("Menor é n1")
        else:
            print("Menor é n2")
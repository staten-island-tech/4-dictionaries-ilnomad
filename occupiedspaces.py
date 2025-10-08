def occupiedspaces():
    n=int(input("Amount of slots? "))
    yesterday=list(input("Occupied spaces yesterday? "))
    today=list(input("Occupied spaces today? "))
    a=0
    print(n,yesterday,today)
    for i in range(n):
        if yesterday[i]==today[i]=="C":
            a=a+1
    print(a)

occupiedspaces()
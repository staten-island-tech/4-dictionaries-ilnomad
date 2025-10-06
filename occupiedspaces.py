def occupiedspaces():
    n=int(input("Amount of slots? "))
    yesterday=list(input("Occupied spaces yesterday? "))
    today=list(input("Occupied spaces today? "))
    z=0
    a=0
    while z==0:
        for n in range(n):
            if yesterday[n]==today[n]:
                a=a+1
    print(a)

occupiedspaces()
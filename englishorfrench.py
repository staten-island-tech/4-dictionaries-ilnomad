def englishorfrench():
    x=input("Type your sentence here. ")
    y=x.split()
    s=0
    t=0

    for y in y:
        if y==("s","S"):
            s=s+1
        elif y==("t","T"):
            t=t+1
    if s>=t:
        print("French")
    elif t>s:
        print("English")

englishorfrench()
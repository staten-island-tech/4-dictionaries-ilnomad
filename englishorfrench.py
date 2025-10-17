def englishorfrench(x):
    s=0
    t=0
    for char in x:
        if char==("s" or "S"):
            s=s+1
        elif char==("t" or "T"):
            t=t+1
    if t>s:
        print("English")
    else:
        print("French")

englishorfrench("st")
steamshop={
    "ID0":{
        "name":"Hollow Knight",
        "Price":"$14.99",
        "Description":"Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes. Explore twisting caverns, battle tainted creatures and befriend bizarre bugs, all in a classic, hand-drawn 2D style.",
    },
    "ID1":{
        "name":"Hollow Knight: Silksong",
        "Price":"$19.99",
        "Description":"Discover a vast, haunted kingdom in Hollow Knight: Silksong! Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.",
    },
    "ID2":{
        "name":"Undertale",
        "Price":"$9.99",
        "Description":"UNDERTALE! The RPG game where you don't have to destroy anyone.",
    },
    "ID3":{
        "name":"Deltarune",
        "Price":"$24.99",
        "Description":"Dive into the parallel story to UNDERTALE! Fight or spare your way through action-packed battles as you explore a mysterious world alongside an endearing cast of new and familiar characters. Chapters 1-4 will be available on launch, with more planned as free updates!",
    }
}

def buysteamshop():
    cart=[]
    ContinueShopping=True
    x=input("Would you like to buy a game? ")
    i=0
    while x==("Yes."):
        while ContinueShopping==True:
            for h in steamshop:
                print(steamshop[h]["name"])
            b=input("What game would you like to buy? ")
            cart.append(b)
            y=input("Would you like to buy another game? ")
            if y=="Yes.":
                ContinueShopping=True
            else:
                x=("No.")
                ContinueShopping=False
    else:
        z=input("Would you like to view your cart or continue shopping? ")
        if z==("Continue shopping."):
            ContinueShopping=True
        elif z==("View my cart."):
            print(cart)
            for i in cart:
                print(steamshop[cart]["Price"])
            

buysteamshop()
steamshop={
    "Hollow Knight":{
        "gameID":0,
        "Price":14.99,
        "Description":"Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes. Explore twisting caverns, battle tainted creatures and befriend bizarre bugs, all in a classic, hand-drawn 2D style.",
    },
    "Hollow Knight: Silksong":{
        "gameID":1,
        "Price":19.99,
        "Description":"Discover a vast, haunted kingdom in Hollow Knight: Silksong! Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.",
    },
    "Undertale":{
        "gameID":2,
        "Price":9.99,
        "Description":"UNDERTALE! The RPG game where you don't have to destroy anyone.",
    },
    "Deltarune":{
        "gameID":3,
        "Price":24.99,
        "Description":"Dive into the parallel story to UNDERTALE! Fight or spare your way through action-packed battles as you explore a mysterious world alongside an endearing cast of new and familiar characters. Chapters 1-4 will be available on launch, with more planned as free updates!",
    }
}

def buysteamshop():
    print("What game would you like to buy?")
    x=input()
    print("What information would you like about the game? (Price or Description)")
    y=input()
    print(steamshop[x][y])

buysteamshop()
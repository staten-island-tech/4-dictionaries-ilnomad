import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

t.speed(2000000)

def a(x):
    for h in range(125):
        for i in range(2):
            t.forward(25+h)
            t.left(90)
        t.right(1)
def b(x):
    for h in range(125):
        for i in range(2):
            t.forward(25+h)
            t.right(90)
        t.left(1)
def c(x):
    t.forward(3*x)
    t.left(120)
    for h in range(3):
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.right(120)
def d(x):
    for h in range(90):
        for i in range(3):
            t.right(120)
            t.forward(x+h^2)
        t.left(7)
def e(x):
    for h in range(45):
        t.forward(x)
        t.left(1)
def f(x):
    for h in range(72):
        for i in range(5):
            t.forward(h)
            t.right(144)
        t.right(11)
def g(x):
    for h in range(90):
        for i in range(21):
            t.forward(h)
            t.right(i*1816+8)
def h(x):
    for i in range(36):
        for h in range(5):
            t.forward(i*5)
            t.left(144)
        t.right(5)
def i(x):
    for h in range(36):
        for i in range(7):
            t.forward(x+h*i)
            t.left(i*9)
def j(x):
    for h in range(x):
        j=0
        j+=1
        t.teleport(0,0)
        t.forward(500)
        for i in range(40):
            t.left(4825*j+5946)
            t.forward(j)
        t.forward(500)
        

#    name=input("What's your name?")
#    print(name)
#def add(x,y):
#    return x+y
#z=add(input("Number Nineteen"), input("Number Eighty Seven"))
#print(z)

#f = "Mason"

#a(200)
#t.teleport(25,25)
#b(200)
#c(50)
#d(100)
#e(0.5)
#f(50)
#g(200)
#h(200)
#i(100)
j(10)

turtle.done()
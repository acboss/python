import turtle
bob = turtle.Turtle()
print(bob)
bob.down()


def poligono(t):
    for i in range(313):
        bob.fd(2)
        bob.lt(1.5)

poligono(bob)
poligono(bob)
turtle.mainloop()
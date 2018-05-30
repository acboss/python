import turtle
bob = turtle.Turtle()
print(bob)
bob.down()


def cerchio(t):
    bob.fd(1)
    bob.lt(7)
    bob.fd(1)
    bob.fd(7)
    bob.lt(1)
    bob.fd(7)
    bob.lt(1)


cerchio(bob)
turtle.mainloop()
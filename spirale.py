import turtle
import math
bob = turtle.Turtle()
theta = 0.0
def spirale(t, n, lunghezza=3, a=0.1, b=0.0002):
   for i in range(n):
        t.fd(3)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta

bob = turtle.Turtle()
spirale(bob, n = 1000)

turtle.mainloop()

print(30/7)
print(30//7)
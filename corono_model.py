import turtle as t

t.color("green")
t.bgcolor("black")
t.speed(11)
t.hideturtle()

def corono(b = 0):
    while b < 200:
        t.right(b)
        t.forward(b*2)
        b = b + 1
corono()
input()
import turtle
t=turtle

length = 5

for i in range(60):
        for i in range(4):
            t.forward(length)
            t.right(90)
        t.right(5)
        length += 5

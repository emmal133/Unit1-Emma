import turtle
t=turtle
x=100
def star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)      
star(100,90)

for i in range(5):
    t.forward(x)
    t.right(144)
    def doubleStars(iRange):
        length=25
        for i in range(iRange):
                star(length,90)
                length=length*2
doubleStars(60)

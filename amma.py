# A tool for me to do color planning for the Amma Cal blanket
# https://www.ravelry.com/patterns/library/amma-cal
from shapes import Paper, Triangle, Rectangle, Oval
from enum import Enum

class Amma(Enum):
    SAGA = 0
    LOLA = 1
    MARIA = 2
    THORA = 3
    TINNA = 4

class AmmaSquare(Rectangle):

    def __init__(self, amma=None, x=0, y=0, color_1="blue", color_2="red", color_3="yellow", color_4="purple"):
        # name of the square in the pattern
        self.amma = amma
        # Aspects of the four squares
        self.rect1 = Rectangle()
        self.rect1.set_width(100)
        self.rect1.set_height(100)
        self.rect1.set_color(color_1)
        self.rect1.x = x
        self.rect1.y = y
        self.rect2 = Rectangle()
        self.rect2.set_width(75)
        self.rect2.set_height(75)
        self.rect2.set_color(color_2)
        self.rect2.x = self.rect1.x + 12.5
        self.rect2.y = self.rect1.y + 12.5
        self.rect3 = Rectangle()
        self.rect3.set_width(50)
        self.rect3.set_height(50)
        self.rect3.set_color(color_3)
        self.rect3.x = self.rect2.x + 12.5
        self.rect3.y = self.rect2.y + 12.5
        self.rect4 = Rectangle()
        self.rect4.set_width(25)
        self.rect4.set_height(25)
        if self.amma != Amma.SAGA:
            self.rect4.set_color(color_4)
        self.rect4.x = self.rect3.x + 12.5
        self.rect4.y = self.rect3.y + 12.5


    def draw(self):
        self.rect1.draw()
        self.rect2.draw()
        self.rect3.draw()
        self.rect4.draw()

# rect1.draw()
# rect2.draw()
# rect3.draw()
# rect4.draw()
paper = Paper()
a1 = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
b1 = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
c1 = AmmaSquare(amma=Amma.TINNA, x=200, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
d1 = AmmaSquare(amma=Amma.TINNA, x=300, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
e1 = AmmaSquare(amma=Amma.TINNA, x=400, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
f1 = AmmaSquare(amma=Amma.TINNA, x=500, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
g1 = AmmaSquare(amma=Amma.TINNA, x=600, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row1 = [a1, b1, c1, d1, e1, f1, g1]

row2= []
# a2 = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row3= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row4= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row5= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row6= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row7= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row8= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
row9= []
# a = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )
# b = AmmaSquare(amma=Amma.TINNA, x=100, y=0, color_1="red", color_2="pink", color_3="yellow", color_4="green" )

blanket=[row1, row2, row3, row4, row5, row6, row7, row8, row9]
for row in blanket:
    for square in row:
        square.draw()
paper.display()

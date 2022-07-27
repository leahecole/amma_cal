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

    def __init__(self, amma=None, x=0, y=0, color_1="white", color_2="white", color_3="white", color_4="white"):
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
        self.rect2.set_width(.75*self.rect1.width)
        self.rect2.set_height(.75*self.rect1.height)
        self.rect2.set_color(color_2)
        self.rect2.x = self.rect1.x + 12.5
        self.rect2.y = self.rect1.y + 12.5
        self.rect3 = Rectangle()
        self.rect3.set_width(.5*self.rect1.width)
        self.rect3.set_height(.5*self.rect1.height)
        self.rect3.set_color(color_3)
        self.rect3.x = self.rect2.x + 12.5
        self.rect3.y = self.rect2.y + 12.5
        self.rect4 = Rectangle()
        self.rect4.set_width(.25*self.rect1.width)
        self.rect4.set_height(.25*self.rect1.height)
        if self.amma == Amma.SAGA:
            self.rect4.set_color(color_1)
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
paper = Paper(width=1000,height=1000)
# TODO(leahecole): generate the coordinates from position
a1 = AmmaSquare(amma=Amma.SAGA, x=0, y=0, color_1="white", color_2="white", color_3="white")
b1 = AmmaSquare(amma=Amma.LOLA, x=100, y=0, color_1="white", color_2="white", color_3="white", color_4="white")
c1 = AmmaSquare(amma=Amma.TINNA, x=200, y=0, color_1="white", color_2="white", color_3="white", color_4="white")
d1 = AmmaSquare(amma=Amma.TINNA, x=300, y=0, color_1="white", color_2="white", color_3="white", color_4="white")
e1 = AmmaSquare(amma=Amma.TINNA, x=400, y=0, color_1="white", color_2="white", color_3="white", color_4="white")
f1 = AmmaSquare(amma=Amma.TINNA, x=500, y=0, color_1="white", color_2="white", color_3="white", color_4="white")
g1 = AmmaSquare(amma=Amma.TINNA, x=600, y=0, color_1="white", color_2="white", color_3="white", color_4="white")
row1 = [a1, b1, c1, d1, e1, f1, g1]

a2 = AmmaSquare(amma=Amma.SAGA, x=0, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
b2 = AmmaSquare(amma=Amma.TINNA, x=100, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
c2 = AmmaSquare(amma=Amma.TINNA, x=200, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
d2 = AmmaSquare(amma=Amma.TINNA, x=300, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
e2 = AmmaSquare(amma=Amma.TINNA, x=400, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
f2 = AmmaSquare(amma=Amma.TINNA, x=500, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
g2 = AmmaSquare(amma=Amma.TINNA, x=600, y=100, color_1="white", color_2="white", color_3="white", color_4="white")
row2 = [a2, b2, c2, d2, e2, f2, g2]

a3 = AmmaSquare(amma=Amma.SAGA, x=0, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
b3 = AmmaSquare(amma=Amma.TINNA, x=100, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
c3 = AmmaSquare(amma=Amma.TINNA, x=200, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
d3 = AmmaSquare(amma=Amma.TINNA, x=300, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
e3 = AmmaSquare(amma=Amma.TINNA, x=400, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
f3 = AmmaSquare(amma=Amma.TINNA, x=500, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
g3 = AmmaSquare(amma=Amma.TINNA, x=600, y=200, color_1="white", color_2="white", color_3="white", color_4="white")
row3 = [a3, b3, c3, d3, e3, f3, g3]

a4 = AmmaSquare(amma=Amma.SAGA, x=0, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
b4 = AmmaSquare(amma=Amma.TINNA, x=100, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
c4 = AmmaSquare(amma=Amma.TINNA, x=200, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
d4 = AmmaSquare(amma=Amma.TINNA, x=300, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
e4 = AmmaSquare(amma=Amma.TINNA, x=400, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
f4 = AmmaSquare(amma=Amma.TINNA, x=500, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
g4 = AmmaSquare(amma=Amma.TINNA, x=600, y=300, color_1="white", color_2="white", color_3="white", color_4="white")
row4 = [a4, b4, c4, d4, e4, f4, g4]

a5 = AmmaSquare(amma=Amma.SAGA, x=0, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
b5 = AmmaSquare(amma=Amma.TINNA, x=100, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
c5 = AmmaSquare(amma=Amma.TINNA, x=200, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
d5 = AmmaSquare(amma=Amma.TINNA, x=300, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
e5 = AmmaSquare(amma=Amma.TINNA, x=400, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
f5 = AmmaSquare(amma=Amma.TINNA, x=500, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
g5 = AmmaSquare(amma=Amma.TINNA, x=600, y=400, color_1="white", color_2="white", color_3="white", color_4="white")
row5 = [a5, b5, c5, d5, e5, f5, g5]

a6 = AmmaSquare(amma=Amma.SAGA, x=0, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
b6 = AmmaSquare(amma=Amma.TINNA, x=100, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
c6 = AmmaSquare(amma=Amma.TINNA, x=200, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
d6 = AmmaSquare(amma=Amma.TINNA, x=300, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
e6 = AmmaSquare(amma=Amma.TINNA, x=400, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
f6 = AmmaSquare(amma=Amma.TINNA, x=500, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
g6 = AmmaSquare(amma=Amma.TINNA, x=600, y=500, color_1="white", color_2="white", color_3="white", color_4="white")
row6 = [a6, b6, c6, d6, e6, f6, g6]

a7 = AmmaSquare(amma=Amma.SAGA, x=0, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
b7 = AmmaSquare(amma=Amma.TINNA, x=100, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
c7 = AmmaSquare(amma=Amma.TINNA, x=200, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
d7 = AmmaSquare(amma=Amma.TINNA, x=300, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
e7 = AmmaSquare(amma=Amma.TINNA, x=400, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
f7 = AmmaSquare(amma=Amma.TINNA, x=500, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
g7 = AmmaSquare(amma=Amma.TINNA, x=600, y=600, color_1="white", color_2="white", color_3="white", color_4="white")
row7 = [a7, b7, c7, d7, e7, f7, g7]

a8 = AmmaSquare(amma=Amma.SAGA, x=0, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
b8 = AmmaSquare(amma=Amma.TINNA, x=100, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
c8 = AmmaSquare(amma=Amma.TINNA, x=200, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
d8 = AmmaSquare(amma=Amma.TINNA, x=300, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
e8 = AmmaSquare(amma=Amma.TINNA, x=400, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
f8 = AmmaSquare(amma=Amma.TINNA, x=500, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
g8 = AmmaSquare(amma=Amma.TINNA, x=600, y=700, color_1="white", color_2="white", color_3="white", color_4="white")
row8 = [a8, b8, c8, d8, e8, f8, g8]

a9 = AmmaSquare(amma=Amma.SAGA, x=0, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
b9 = AmmaSquare(amma=Amma.TINNA, x=100, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
c9 = AmmaSquare(amma=Amma.TINNA, x=200, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
d9 = AmmaSquare(amma=Amma.TINNA, x=300, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
e9 = AmmaSquare(amma=Amma.TINNA, x=400, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
f9 = AmmaSquare(amma=Amma.TINNA, x=500, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
g9 = AmmaSquare(amma=Amma.TINNA, x=600, y=800, color_1="white", color_2="white", color_3="white", color_4="white")
row9 = [a9, b9, c9, d9, e9, f9, g9]


blanket=[row1, row2, row3, row4, row5, row6, row7, row8, row9]
for row in blanket:
    for square in row:
        square.draw()
paper.display()

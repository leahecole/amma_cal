# A tool for me to do color planning for the Amma Cal blanket
# https://www.ravelry.com/patterns/library/amma-cal
from shapes import Paper, Triangle, Rectangle, Oval
from enum import Enum, unique



# there are five types of squares named after grandmas
class Amma(Enum):
    SAGA = 0
    LOLA = 1
    MARIA = 2
    THORA = 3
    TINNA = 4

# colors that will be used which correspond to the "Happy Granny" colorway
@unique
class Color(Enum):
    CURRY = "#CB9834"
    ORANGE = "#F76A25"
    RUSTIC_RED = "#C50909"
    PINK = "#E264B7"
    PURPLE = "#7A1FAE"
    ROYAL_BLUE = "#295198"
    TURQUOISE = "#2DBBDE"
    TEAL = "#236A65"
    BASE = "#E7D8BB"

# CONSTANTS
SQUARE_WIDTH = 50

class AmmaSquare(Rectangle):

    def __init__(self, amma=None, row=0, col=0, color_1=Color.BASE, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE):
        # name of the square in the pattern
        self.amma = amma
        self.row = row
        self.col = col
        # Aspects of the four squares
        self.rect1 = Rectangle()
        self.rect1.set_width(SQUARE_WIDTH)
        self.rect1.set_height(SQUARE_WIDTH)
        interval = self.rect1.width/8 #calculate the offset between squares
        self.rect1.color_name = color_1.name
        self.rect1.set_color(color_1.value)
        self.rect1.x = (col-1) * self.rect1.width
        self.rect1.y = (row-1) * self.rect1.width
        self.rect2 = Rectangle()
        self.rect2.set_width(.75*self.rect1.width)
        self.rect2.set_height(.75*self.rect1.height)
        self.rect2.color_name = color_2.name
        self.rect2.set_color(color_2.value)
        self.rect2.x = self.rect1.x + interval
        self.rect2.y = self.rect1.y + interval
        self.rect3 = Rectangle()
        self.rect3.set_width(.5*self.rect1.width)
        self.rect3.set_height(.5*self.rect1.height)
        self.rect3.color_name = color_3.name
        self.rect3.set_color(color_3.value)
        self.rect3.x= self.rect2.x + interval
        self.rect3.y = self.rect2.y + interval
        self.rect4 = Rectangle()
        self.rect4.set_width(.25*self.rect1.width)
        self.rect4.set_height(.25*self.rect1.height)
        # SAGA squares have the base color at the center
        if self.amma == Amma.SAGA:
            self.rect4.color_name = Color.BASE.name
            self.rect4.set_color(Color.BASE.value) 
        else: 
            self.rect4.color_name = color_4.name
            self.rect4.set_color(color_4.value)
        self.rect4.x = self.rect3.x + interval
        self.rect4.y = self.rect3.y + interval

    # A function that prints the Amma object as a dictionary
    def display(self):
        readable_amma = {
            "Amma": self.amma.name,
            "Color 1": self.rect1.color_name,
            "Color 2": self.rect2.color_name,
            "Color 3": self.rect3.color_name,
            "Color 4": self.rect4.color_name,
            "Row": self.row,
            "Column": self.col
        }
        return readable_amma

    def draw(self):
        self.rect1.draw()
        self.rect2.draw()
        self.rect3.draw()
        self.rect4.draw()

def makeAmmaFromDict(ammaDict):
    return AmmaSquare(amma=Amma[ammaDict["Amma"]], row=ammaDict["Row"], col=ammaDict["Column"], color_1=Color[ammaDict["Color 1"]], color_2=Color[ammaDict["Color 2"]], color_3=Color[ammaDict["Color 3"]], color_4=Color[ammaDict["Color 4"]])

paper = Paper(width=1000,height=1000)
# TODO(leahecole): update colors
a1 = AmmaSquare(amma=Amma.SAGA, row=1, col=1, color_2=Color.CURRY, color_3=Color.ROYAL_BLUE)
b1 = AmmaSquare(amma=Amma.LOLA, row=1, col=2, color_2=Color.RUSTIC_RED, color_3=Color.BASE, color_4=Color.BASE)
c1 = AmmaSquare(amma=Amma.MARIA, row=1, col=3,  color_2=Color.ORANGE, color_3=Color.BASE, color_4=Color.BASE)
d1 = AmmaSquare(amma=Amma.THORA, row=1, col=4, color_2=Color.TURQUOISE, color_3=Color.BASE, color_4=Color.BASE)
e1 = AmmaSquare(amma=Amma.TINNA, row=1, col=5, color_2=Color.TEAL, color_3=Color.BASE, color_4=Color.BASE)
f1 = AmmaSquare(amma=Amma.SAGA, row=1, col=6, color_2=Color.PINK, color_3=Color.BASE, color_4=Color.BASE)
g1 = AmmaSquare(amma=Amma.LOLA, row=1, col=7, color_2=Color.PURPLE, color_3=Color.BASE, color_4=Color.BASE)
row1 = [a1, b1, c1, d1, e1, f1, g1]

a2 = AmmaSquare(amma=Amma.LOLA, row=2, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b2 = AmmaSquare(amma=Amma.MARIA, row=2, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c2 = AmmaSquare(amma=Amma.THORA, row=2, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d2 = AmmaSquare(amma=Amma.TINNA, row=2, col=4, color_2=Color.RUSTIC_RED, color_3=Color.BASE, color_4=Color.BASE)
e2 = AmmaSquare(amma=Amma.SAGA, row=2, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f2 = AmmaSquare(amma=Amma.LOLA, row=2, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g2 = AmmaSquare(amma=Amma.MARIA, row=2, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row2 = [a2, b2, c2, d2, e2, f2, g2]

a3 = AmmaSquare(amma=Amma.MARIA, row=3, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b3 = AmmaSquare(amma=Amma.THORA, row=3, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c3 = AmmaSquare(amma=Amma.TINNA, row=3, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d3 = AmmaSquare(amma=Amma.SAGA, row=3, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e3 = AmmaSquare(amma=Amma.LOLA, row=3, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f3 = AmmaSquare(amma=Amma.MARIA, row=3, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g3 = AmmaSquare(amma=Amma.THORA, row=3, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row3 = [a3, b3, c3, d3, e3, f3, g3]

a4 = AmmaSquare(amma=Amma.THORA, row=4, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b4 = AmmaSquare(amma=Amma.TINNA, row=4, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c4 = AmmaSquare(amma=Amma.SAGA, row=4, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d4 = AmmaSquare(amma=Amma.LOLA, row=4, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e4 = AmmaSquare(amma=Amma.MARIA, row=4, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f4 = AmmaSquare(amma=Amma.THORA, row=4, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g4 = AmmaSquare(amma=Amma.TINNA, row=4, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row4 = [a4, b4, c4, d4, e4, f4, g4]

a5 = AmmaSquare(amma=Amma.TINNA, row=5, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b5 = AmmaSquare(amma=Amma.SAGA, row=5, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c5 = AmmaSquare(amma=Amma.LOLA, row=5, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d5 = AmmaSquare(amma=Amma.MARIA, row=5, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e5 = AmmaSquare(amma=Amma.THORA, row=5, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f5 = AmmaSquare(amma=Amma.TINNA, row=5, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g5 = AmmaSquare(amma=Amma.SAGA, row=5, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row5 = [a5, b5, c5, d5, e5, f5, g5]

a6 = AmmaSquare(amma=Amma.SAGA, row=6, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b6 = AmmaSquare(amma=Amma.LOLA, row=6, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c6 = AmmaSquare(amma=Amma.MARIA, row=6, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d6 = AmmaSquare(amma=Amma.THORA, row=6, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e6 = AmmaSquare(amma=Amma.TINNA, row=6, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f6 = AmmaSquare(amma=Amma.SAGA, row=6, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g6 = AmmaSquare(amma=Amma.LOLA, row=6, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row6 = [a6, b6, c6, d6, e6, f6, g6]

a7 = AmmaSquare(amma=Amma.LOLA, row=7, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b7 = AmmaSquare(amma=Amma.MARIA, row=7, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c7 = AmmaSquare(amma=Amma.THORA, row=7, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d7 = AmmaSquare(amma=Amma.TINNA, row=7, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e7 = AmmaSquare(amma=Amma.SAGA, row=7, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f7 = AmmaSquare(amma=Amma.LOLA, row=7, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g7 = AmmaSquare(amma=Amma.MARIA, row=7, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row7 = [a7, b7, c7, d7, e7, f7, g7]

a8 = AmmaSquare(amma=Amma.MARIA, row=8, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b8 = AmmaSquare(amma=Amma.THORA, row=8, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c8 = AmmaSquare(amma=Amma.TINNA, row=8, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d8 = AmmaSquare(amma=Amma.SAGA, row=8, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e8 = AmmaSquare(amma=Amma.LOLA, row=8, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f8 = AmmaSquare(amma=Amma.MARIA, row=8, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g8 = AmmaSquare(amma=Amma.THORA, row=8, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row8 = [a8, b8, c8, d8, e8, f8, g8]

a9 = AmmaSquare(amma=Amma.THORA, row=9, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
b9 = AmmaSquare(amma=Amma.TINNA, row=9, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
c9 = AmmaSquare(amma=Amma.SAGA, row=9, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
d9 = AmmaSquare(amma=Amma.LOLA, row=9, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
e9 = AmmaSquare(amma=Amma.MARIA, row=9, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
f9 = AmmaSquare(amma=Amma.THORA, row=9, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
g9 = AmmaSquare(amma=Amma.TINNA, row=9, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
row9 = [a9, b9, c9, d9, e9, f9, g9]


blanket=[row1, row2, row3, row4, row5, row6, row7, row8, row9]
for row in blanket:
    for square in row:
        square.draw()

def count_colors(squares):
    #count
    rect2 = {}
    rect3 = {}
    rect4 = {}
    for row in squares:
        for square in row:
            try:
                rect2[square.rect2.color_name] += 1
            except KeyError:
                rect2[square.rect2.color_name] = 1
            try:
                rect3[square.rect3.color_name] += 1
            except KeyError:
                rect3[square.rect3.color_name] = 1
            try:
                rect4[square.rect4.color_name] += 1
            except KeyError:
                rect4[square.rect4.color_name] = 1

    

    #display results
    print(f"rect2 counts: {rect2}")
    print(f"rect3 counts: {rect3}")
    print(f"rect4 counts:{rect4}")
count_colors(blanket)
print(a1.display())
paper.display()

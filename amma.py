# A tool for me to do color planning for the Amma Cal blanket
# https://www.ravelry.com/patterns/library/amma-cal
from shapes import Paper, Rectangle, Shape
from enum import Enum, unique
import random



# there are five types of squares named after grandmas
class Amma(Enum):
    SAGA = 0
    LOLA = 1
    MARIA = 2
    THORA = 3
    TINNA = 4

# colors that will be used which correspond to the "Happy Granny" colorway
# I eyeballed hex values based on what I saw in the pattern
# These will be yarns from the Scheepjes Stone Washed/River Washed line
# https://www.scheepjes.com/en/stone-washed-440/
# https://www.scheepjes.com/en/river-washed-2317/

@unique
class Color(Enum):
    CURRY = "#CB9834" # stone washed 812 lemon quartz
    ORANGE = "#F76A25" # River Washed 961
    RUSTIC_RED = "#C50909" # River washed 956
    PINK = "#E264B7" # Stone Washed 836
    PURPLE = "#6B0CEB" # River Washed 949 (to add)
    ROYAL_BLUE = "#0B8DD0" #stone washed 805
    TURQUOISE = "#2DBBDE" # River washed 950
    TEAL = "#108E45" # River Washed 958
    BASE = "#FFFAF6" # Moon stone

# CONSTANTS
SQUARE_WIDTH = 50
COLOR_LIST = list(Color) #generate a list so we can use random integers to select a color

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


    def display(self) -> dict:
        """
        Prints the parts of the Amma object I care about as a dictionary

        """
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

    def display_colors(self) -> dict:
        # TODO: remove if not actually used?
        colors = self.display()
        del(colors["Amma"])
        del(colors["Row"])
        del(colors["Column"])
        return colors

    def draw(self) -> None:
        self.rect1.draw()
        self.rect2.draw()
        self.rect3.draw()
        self.rect4.draw()

def ammaEquals(square1: AmmaSquare, square2: AmmaSquare) -> bool:
    #TODO: refactor, this is not working properly and my brain is too tired
    """
    Compare two Amma squares to determine if they are equal
    """
    # they must have different row and columns

    if (square1["Row"]==square2["Row"]) or (square2["Column"]==square2["Column"]):
        # if they have the same colors
        # square type does not matter
        if (square1["Color 1"]==square2["Color 1"]) and \
           (square1["Color 2"]==square2["Color 2"]) and \
           (square1["Color 3"]==square2["Color 3"]) and \
           (square1["Color 4"]==square2["Color 4"]):
           return True
        else:
            return False
    else:
        return False


def lookForDupes(blanket:list) -> list:
    dupes = []
    for i in range(0, len(blanket)):
        square1 = blanket[i]
        for j in range(i+1, len(blanket)):
            square2 = blanket[j]
            if (i!=j) and (ammaEquals(square1, square2)):
                dupes.append(square1)
                dupes.append(square2)
    return dupes
# run this on a single dict representing a square   
def makeAmmaSquareFromDict(ammaDict):
    return AmmaSquare(amma=Amma[ammaDict["Amma"]], row=ammaDict["Row"], col=ammaDict["Column"], color_1=Color[ammaDict["Color 1"]], color_2=Color[ammaDict["Color 2"]], color_3=Color[ammaDict["Color 3"]], color_4=Color[ammaDict["Color 4"]])

def makeAmmaBlanketFromReadableBlanketList(readable_blanket: list):
    blanket = []
    for square_dict in readable_blanket:
        blanket.append(makeAmmaSquareFromDict(square_dict))
    return blanket


def count_colors(squares: list) -> None:
    """
    squares: a list of lists of Amma squares
    makes dictionaries for rect2, rect3, rect4, 
    prints counts for each
    """
    #count
    rect2 = {}
    rect3 = {}
    rect4 = {}
    for square in squares:
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

    totals = {}
    for key in rect2.keys():
        try:
            totals[key] += rect2[key]
        except KeyError:
            totals[key] = rect2[key]
    #this is guaranteed to not have KeyErrors if it runs after rect2 
    #so I'm not checking because I'm lazy
    for key in rect3.keys(): 
        totals[key] += rect3[key]
    #this could throw a keyerror because it introduces "Base" as an option
    for key in rect4.keys(): 
        try:
            totals[key] += rect4[key]
        except KeyError:
            totals[key] = rect4[key]
    

    #display results
    #print(f"rect2 counts: {rect2}")
    #print(f"rect3 counts: {rect3}")
    #print(f"rect4 counts:{rect4}")
    #print(f"totals: {totals}")

# Display dicts of final blanket
#TODO refactor to not rely on nested list structure
# NOTE THIS CURRENTLY WON'T WORK
def display_blanket_dict(blanket):
    column = ["a", "b", "c", "d", "e", "f", "g"]

    for row in range(len(blanket)):
        for square in range(len(blanket[row])):
            print(f"{str(column[square])}{str(row+1)} = {blanket[row][square].display()}")

def draw_blanket(blanket: list, paper: Paper) -> Paper:
    """
    blanket: list of list of AmmaSquare objects
    goes through each square and "draws" it
    returns the paper to be displayed in the main method
    """
    for square in blanket:
        square.draw()
    #paper.display()
    return paper


def random_blanket_algorithm(blanket):
    # this is a stupid algorithm that only generates random color patterns

    for square in blanket:
        choices = [0,1,2,3,4,5,6,7]
        choice_1 = random.choice(choices) #only choose between non base colors
        choices.remove(choice_1)
        choice_2 = random.choice(choices)
        choices.remove(choice_2)
        choice_3 = random.choice(choices)
        color_choice_1 = COLOR_LIST[choice_1]
        color_choice_2 = COLOR_LIST[choice_2]
        color_choice_3 = COLOR_LIST[choice_3]
        square.rect2.set_color(color_choice_1.value)
        square.rect2.color_name = color_choice_1.name 
        square.rect3.set_color(color_choice_2.value)
        square.rect3.color_name = color_choice_2.name
        if square.amma != Amma.SAGA: #TODO: move this logic elsewhere
            square.rect4.set_color(color_choice_3.value)
            square.rect4.color_name = color_choice_3.name 

    return blanket

def even_distro_blanket_algorithm(blanket):
    squares = {}

    rect2 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    rect3 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    rect4 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    # this is an algorithm to make even color distrubition in each row. I refactored it while very tired and it's very ugly
    def remove_choice(choices, choice):
        try:
            choices.remove(choice)
        except ValueError:
            log = f"Choice {choice} not in choices. Likely ineligible for other reasons"
            #print(log)
        finally:
            return choices
    def set_color(square):
        #TODO: fix occasional IndexError

        # sets the colors but also returns a 3 number color that can be used for tracking
        # choose color one from all of the colors, as long as it hasn't been used 8 times
        choices = [choice for choice in rect2.keys() if rect2[choice] < 8]      

        choice_1 = random.choice(choices) #only choose between non base colors
        rect2[choice_1]+=1
        
        # choose color 2 from all of the colors as long as it hasn't been used 8 times
        # and it wasn't color 1
        choices = [choice for choice in rect3.keys() if rect3[choice] < 8]  
  
        choices = remove_choice(choices, choice_1)   
        choice_2 = random.choice(choices)
        rect3[choice_2]+=1

        # choose color 3 from all of the colors as long as it hasn't been used 7 times
        # and it wasn't color 1 or color 2
        choices = [choice for choice in rect4.keys() if rect4[choice] < 7] #this limit is smaller because there are only 51 possible squares instead of 63 like in other rounds       

        choices = remove_choice(choices, choice_1) 
        choices = remove_choice(choices, choice_2)   
        choice_3 = random.choice(choices)

        # Actually get the color
        color_choice_1 = COLOR_LIST[choice_1]
        color_choice_2 = COLOR_LIST[choice_2]
        color_choice_3 = COLOR_LIST[choice_3]

        # set the appropriate attributes of the squares
        square.rect2.set_color(color_choice_1.value)
        square.rect2.color_name = color_choice_1.name 
        square.rect3.set_color(color_choice_2.value)
        square.rect3.color_name = color_choice_2.name

        if square.amma != Amma.SAGA: #TODO: move this logic elsewhere
            square.rect4.set_color(color_choice_3.value)
            square.rect4.color_name = color_choice_3.name
            rect4[choice_3]+=1
        return f"{choice_1}{choice_2}{choice_3}"

    # this makes an even distro but it doesn't return the object when it's done
    def even_distro_no_repeats(squares: dict, blanket:list, blanket_out:list) -> list:
        print("blanket", len(blanket))
    # base case - there are no squares left, return
        if len(blanket) == 0:
            return blanket_out
        else:
            colors = set_color(blanket[0])
            print("colors", colors)
            try:
                squares[colors] # this will be a KeyError if it hasn't been used
                # remove colors from rect dicts - colors is a 3 digit integer
                # these were incremented as part of set_color, and we don't want this to last
                print("squares[colors]", squares[colors])
                rect2[int(colors[0])]-=1
                rect3[int(colors[1])]-=1
                rect4[int(colors[2])]-=1
                return even_distro_no_repeats(squares, blanket, blanket_out)
            except KeyError:
                squares[colors] = 1
                blanket_out.append(blanket[0])
                return even_distro_no_repeats(squares, blanket[1:], blanket_out)
    blanket = even_distro_no_repeats(squares,blanket, [])
            
    print("squares", squares)
    print('squares keys', len(squares.keys()))
    # print(f"{rect2}, {rect3}, {rect4}")
    return blanket, squares



if __name__ == "__main__":
    paper = Paper(width=1000,height=1000)

    # 
    # Example Amma Squares
    a1 = AmmaSquare(amma=Amma.SAGA, row=1, col=1, color_2=Color.CURRY, color_3=Color.ROYAL_BLUE)
    b1 = AmmaSquare(amma=Amma.LOLA, row=1, col=2, color_2=Color.RUSTIC_RED, color_3=Color.BASE, color_4=Color.BASE)
    c1 = AmmaSquare(amma=Amma.MARIA, row=1, col=3,  color_2=Color.ORANGE, color_3=Color.BASE, color_4=Color.BASE)
    d1 = AmmaSquare(amma=Amma.THORA, row=1, col=4, color_2=Color.TURQUOISE, color_3=Color.BASE, color_4=Color.BASE)
    e1 = AmmaSquare(amma=Amma.TINNA, row=1, col=5, color_2=Color.TEAL, color_3=Color.BASE, color_4=Color.BASE)
    f1 = AmmaSquare(amma=Amma.SAGA, row=1, col=6, color_2=Color.PINK, color_3=Color.BASE, color_4=Color.BASE)
    g1 = AmmaSquare(amma=Amma.LOLA, row=1, col=7, color_2=Color.PURPLE, color_3=Color.BASE, color_4=Color.BASE)

    a2 = AmmaSquare(amma=Amma.LOLA, row=2, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b2 = AmmaSquare(amma=Amma.MARIA, row=2, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c2 = AmmaSquare(amma=Amma.THORA, row=2, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d2 = AmmaSquare(amma=Amma.TINNA, row=2, col=4, color_2=Color.RUSTIC_RED, color_3=Color.BASE, color_4=Color.BASE)
    e2 = AmmaSquare(amma=Amma.SAGA, row=2, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f2 = AmmaSquare(amma=Amma.LOLA, row=2, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g2 = AmmaSquare(amma=Amma.MARIA, row=2, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a3 = AmmaSquare(amma=Amma.MARIA, row=3, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b3 = AmmaSquare(amma=Amma.THORA, row=3, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c3 = AmmaSquare(amma=Amma.TINNA, row=3, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d3 = AmmaSquare(amma=Amma.SAGA, row=3, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e3 = AmmaSquare(amma=Amma.LOLA, row=3, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f3 = AmmaSquare(amma=Amma.MARIA, row=3, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g3 = AmmaSquare(amma=Amma.THORA, row=3, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a4 = AmmaSquare(amma=Amma.THORA, row=4, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b4 = AmmaSquare(amma=Amma.TINNA, row=4, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c4 = AmmaSquare(amma=Amma.SAGA, row=4, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d4 = AmmaSquare(amma=Amma.LOLA, row=4, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e4 = AmmaSquare(amma=Amma.MARIA, row=4, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f4 = AmmaSquare(amma=Amma.THORA, row=4, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g4 = AmmaSquare(amma=Amma.TINNA, row=4, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a5 = AmmaSquare(amma=Amma.TINNA, row=5, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b5 = AmmaSquare(amma=Amma.SAGA, row=5, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c5 = AmmaSquare(amma=Amma.LOLA, row=5, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d5 = AmmaSquare(amma=Amma.MARIA, row=5, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e5 = AmmaSquare(amma=Amma.THORA, row=5, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f5 = AmmaSquare(amma=Amma.TINNA, row=5, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g5 = AmmaSquare(amma=Amma.SAGA, row=5, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a6 = AmmaSquare(amma=Amma.SAGA, row=6, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b6 = AmmaSquare(amma=Amma.LOLA, row=6, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c6 = AmmaSquare(amma=Amma.MARIA, row=6, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d6 = AmmaSquare(amma=Amma.THORA, row=6, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e6 = AmmaSquare(amma=Amma.TINNA, row=6, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f6 = AmmaSquare(amma=Amma.SAGA, row=6, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g6 = AmmaSquare(amma=Amma.LOLA, row=6, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a7 = AmmaSquare(amma=Amma.LOLA, row=7, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b7 = AmmaSquare(amma=Amma.MARIA, row=7, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c7 = AmmaSquare(amma=Amma.THORA, row=7, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d7 = AmmaSquare(amma=Amma.TINNA, row=7, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e7 = AmmaSquare(amma=Amma.SAGA, row=7, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f7 = AmmaSquare(amma=Amma.LOLA, row=7, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g7 = AmmaSquare(amma=Amma.MARIA, row=7, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a8 = AmmaSquare(amma=Amma.MARIA, row=8, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b8 = AmmaSquare(amma=Amma.THORA, row=8, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c8 = AmmaSquare(amma=Amma.TINNA, row=8, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d8 = AmmaSquare(amma=Amma.SAGA, row=8, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e8 = AmmaSquare(amma=Amma.LOLA, row=8, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f8 = AmmaSquare(amma=Amma.MARIA, row=8, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g8 = AmmaSquare(amma=Amma.THORA, row=8, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)

    a9 = AmmaSquare(amma=Amma.THORA, row=9, col=1, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    b9 = AmmaSquare(amma=Amma.TINNA, row=9, col=2, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    c9 = AmmaSquare(amma=Amma.SAGA, row=9, col=3, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    d9 = AmmaSquare(amma=Amma.LOLA, row=9, col=4, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    e9 = AmmaSquare(amma=Amma.MARIA, row=9, col=5, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    f9 = AmmaSquare(amma=Amma.THORA, row=9, col=6, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    g9 = AmmaSquare(amma=Amma.TINNA, row=9, col=7, color_2=Color.BASE, color_3=Color.BASE, color_4=Color.BASE)
    
    # Example layout
    row1 = [a1, b1, c1, d1, e1, f1, g1]
    row2 = [a2, b2, c2, d2, e2, f2, g2]
    row3 = [a3, b3, c3, d3, e3, f3, g3]
    row4 = [a4, b4, c4, d4, e4, f4, g4]
    row5 = [a5, b5, c5, d5, e5, f5, g5]
    row6 = [a6, b6, c6, d6, e6, f6, g6]
    row7 = [a7, b7, c7, d7, e7, f7, g7]
    row8 = [a8, b8, c8, d8, e8, f8, g8]
    row9 = [a9, b9, c9, d9, e9, f9, g9]

    # blanket = row1+row2+row3
    blanket = row1+row2+row3+row4+row5+row6+row7+row8+row9
    blanket = random_blanket_algorithm(blanket)
    # blanket,squares = even_distro_blanket_algorithm(blanket)

    count_colors(blanket)

    # make something readable that I can edit and pass back in
    readable_blanket = []
    for square in blanket:
        s = square.display()
        readable_blanket.append(s)
    print(readable_blanket)
    print(lookForDupes(readable_blanket))

    p = draw_blanket(blanket, paper)
    p.display()


    # example = [{'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'CURRY', 'Color 4': 'BASE', 'Row': 1, 'Column': 1}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'PINK', 'Color 4': 'TURQUOISE', 'Row': 1, 'Column': 2}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'ORANGE', 'Color 4': 'PURPLE', 'Row': 1, 'Column': 3}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'RUSTIC_RED', 'Row': 1, 'Column': 4}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'RUSTIC_RED', 'Row': 1, 'Column': 5}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'PINK', 'Color 4': 'BASE', 'Row': 1, 'Column': 6}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'CURRY', 'Color 4': 'PINK', 'Row': 1, 'Column': 7}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'CURRY', 'Color 4': 'PURPLE', 'Row': 2, 'Column': 1}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'RUSTIC_RED', 'Color 4': 'ORANGE', 'Row': 2, 'Column': 2}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'PURPLE', 'Color 4': 'CURRY', 'Row': 2, 'Column': 3}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'TURQUOISE', 'Row': 2, 'Column': 4}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'PINK', 'Color 4': 'BASE', 'Row': 2, 'Column': 5}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'CURRY', 'Color 4': 'ORANGE', 'Row': 2, 'Column': 6}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'PURPLE', 'Color 4': 'TEAL', 'Row': 2, 'Column': 7}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'PINK', 'Color 4': 'ORANGE', 'Row': 3, 'Column': 1}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'CURRY', 'Color 4': 'TEAL', 'Row': 3, 'Column': 2}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'RUSTIC_RED', 'Color 4': 'PURPLE', 'Row': 3, 'Column': 3}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'PINK', 'Color 4': 'BASE', 'Row': 3, 'Column': 4}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'RUSTIC_RED', 'Color 4': 'TURQUOISE', 'Row': 3, 'Column': 5}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'TEAL', 'Color 4': 'ORANGE', 'Row': 3, 'Column': 6}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'PINK', 'Color 4': 'CURRY', 'Row': 3, 'Column': 7}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'ORANGE', 'Color 4': 'RUSTIC_RED', 'Row': 4, 'Column': 1}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'ORANGE', 'Color 4': 'RUSTIC_RED', 'Row': 4, 'Column': 2}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'PURPLE', 'Color 4': 'BASE', 'Row': 4, 'Column': 3}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'RUSTIC_RED', 'Color 4': 'ROYAL_BLUE', 'Row': 4, 'Column': 4}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'PINK', 'Row': 4, 'Column': 5}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'PINK', 'Row': 4, 'Column': 6}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'PINK', 'Color 4': 'TEAL', 'Row': 4, 'Column': 7}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'CURRY', 'Color 4': 'RUSTIC_RED', 'Row': 5, 'Column': 1}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'PINK', 'Color 4': 'BASE', 'Row': 5, 'Column': 2}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'PURPLE', 'Color 4': 'ROYAL_BLUE', 'Row': 5, 'Column': 3}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'PURPLE', 'Color 4': 'ORANGE', 'Row': 5, 'Column': 4}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'TURQUOISE', 'Color 4': 'RUSTIC_RED', 'Row': 5, 'Column': 5}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'ORANGE', 'Color 4': 'RUSTIC_RED', 'Row': 5, 'Column': 6}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'TEAL', 'Color 4': 'BASE', 'Row': 5, 'Column': 7}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'RUSTIC_RED', 'Color 4': 'BASE', 'Row': 6, 'Column': 1}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'TURQUOISE', 'Color 4': 'CURRY', 'Row': 6, 'Column': 2}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'TEAL', 'Color 4': 'CURRY', 'Row': 6, 'Column': 3}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'CURRY', 'Color 4': 'ORANGE', 'Row': 6, 'Column': 4}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'PURPLE', 'Color 4': 'TEAL', 'Row': 6, 'Column': 5}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'TEAL', 'Color 4': 'BASE', 'Row': 6, 'Column': 6}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'TEAL', 'Color 4': 'TURQUOISE', 'Row': 6, 'Column': 7}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'ORANGE', 'Color 4': 'ROYAL_BLUE', 'Row': 7, 'Column': 1}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'CURRY', 'Color 3': 'TURQUOISE', 'Color 4': 'PURPLE', 'Row': 7, 'Column': 2}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'PURPLE', 'Color 4': 'ROYAL_BLUE', 'Row': 7, 'Column': 3}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'RUSTIC_RED', 'Color 4': 'ROYAL_BLUE', 'Row': 7, 'Column': 4}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'TEAL', 'Color 4': 'BASE', 'Row': 7, 'Column': 5}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'CURRY', 'Color 4': 'TURQUOISE', 'Row': 7, 'Column': 6}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'PURPLE', 'Row': 7, 'Column': 7}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'TURQUOISE', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'ORANGE', 'Row': 8, 'Column': 1}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'PURPLE', 'Color 4': 'ROYAL_BLUE', 'Row': 8, 'Column': 2}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'RUSTIC_RED', 'Color 4': 'TURQUOISE', 'Row': 8, 'Column': 3}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'TURQUOISE', 'Color 4': 'BASE', 'Row': 8, 'Column': 4}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'ROYAL_BLUE', 'Color 4': 'CURRY', 'Row': 8, 'Column': 5}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'ORANGE', 'Color 4': 'PURPLE', 'Row': 8, 'Column': 6}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'ORANGE', 'Color 4': 'PINK', 'Row': 8, 'Column': 7}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'TEAL', 'Color 3': 'RUSTIC_RED', 'Color 4': 'ROYAL_BLUE', 'Row': 9, 'Column': 1}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'TEAL', 'Color 4': 'CURRY', 'Row': 9, 'Column': 2}, {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'RUSTIC_RED', 'Color 3': 'TEAL', 'Color 4': 'BASE', 'Row': 9, 'Column': 3}, {'Amma': 'LOLA', 'Color 1': 'BASE', 'Color 2': 'ORANGE', 'Color 3': 'TURQUOISE', 'Color 4': 'PINK', 'Row': 9, 'Column': 4}, {'Amma': 'MARIA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'ORANGE', 'Color 4': 'TURQUOISE', 'Row': 9, 'Column': 5}, {'Amma': 'THORA', 'Color 1': 'BASE', 'Color 2': 'PINK', 'Color 3': 'TURQUOISE', 'Color 4': 'TEAL', 'Row': 9, 'Column': 6}, {'Amma': 'TINNA', 'Color 1': 'BASE', 'Color 2': 'ROYAL_BLUE', 'Color 3': 'TURQUOISE', 'Color 4': 'TEAL', 'Row': 9, 'Column': 7}]
    # print("dupes")
    # a = lookForDupes(example)
    # print(lookForDupes(example))
    # a = {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'PINK', 'Color 4': 'BASE', 'Row': 1, 'Column': 6}
    # b = {'Amma': 'SAGA', 'Color 1': 'BASE', 'Color 2': 'PURPLE', 'Color 3': 'PINK', 'Color 4': 'BASE', 'Row': 2, 'Column': 5}
    # print(example[0], example[1])
    # print(ammaEquals(example[0], example[1]))
    # example drawing a blanket made from a readable list
    # blanket2 = makeAmmaBlanketFromReadableBlanketList(example)
    # p = draw_blanket(blanket2, paper)
    # p.display()


    

    #display_blanket_dict(readable_blanket)

